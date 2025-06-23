''' Module for preparing 311 service requests concering homelessness'''

import pandas as pd
from pyproj import Transformer
import geopandas as gpd
from shapely.geometry import Point

def get_preped_311_data():
    '''Prepare 311 data for project'''
    # read in original data
    df = pd.read_csv('311_service_requests.csv')
    
    # Get relevant columns
    df = df[['OPENEDDATETIME',
             'TYPENAME', 
             'XCOORD',
             'YCOORD']]


    df = df.rename(columns = {'OPENEDDATETIME' : 'open_date',
                              'TYPENAME' : 'type',  
                              'Council District' : 'district',
                              'XCOORD' : 'x_coord',
                              'YCOORD' : 'y_coord'})
    
    # keep only rows with values in type column that are associated with homelessness
    homeless = ['Homeless Encampment',
                'Homeless Outreach',
                'Encampment Abatement',
                'Sanitation_Encampment_Abatement',
                'Sanitation_UF-Encampment Abatement',
                'Sanitation_NA-Encampment Abatement']
    
    df = df[df['type'].isin(homeless)].reset_index(drop=True)
    
    # convert coordinates to latitude and longitude
    # define transformer: from EPSG:2278 (Texas South Central, ft) to EPSG:4326 (WGS84)
    transformer = Transformer.from_crs("EPSG:2278", "EPSG:4326", always_xy=True)

    # create new columns using x and y _coord columns
    df["longitude"], df["latitude"] = transformer.transform(df["x_coord"].values, df["y_coord"].values)

    # drop original coordinates
    df = df.drop(columns =['x_coord','y_coord'])
    
    # get zipcodes
    # get list with Point(longitude, latitude) for data frame
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]

    # convert df to geodataframe
    gdf_points = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

    # load 2024 ZCTA shapefile into a geodataframe
    gdf_zips = gpd.read_file('tl_2024_us_zcta520.shp')

    # ensure both geoDataFrames use the same CRS
    gdf_zips = gdf_zips.to_crs(gdf_points.crs)

    # spatialy join geodataframes adding zipcode info to gdf_points
    gdf_joined = gpd.sjoin(gdf_points, gdf_zips, how='left', predicate='within')

    # add ZIP code column from shapefile 
    gdf_joined['zip_code'] = gdf_joined['ZCTA5CE20'] 
    
    # drop spatial join metadata
    gdf_joined = gdf_joined.drop(columns=['index_right'])

    # convert back to regular dataframe
    df = pd.DataFrame(gdf_joined)

    # drop parsing columns
    df = df[['open_date',
             'type',
             'latitude',
             'longitude',
             'zip_code']]
    
    # drop rows with zipcodes not in San Antonio
    # list of zips in San Antonio
    sa_zips = ['78201', '78202', '78203', '78204', '78205', 
               '78206', '78207', '78208', '78209', '78210', 
               '78211', '78212', '78213', '78214', '78215', 
               '78216', '78217', '78218', '78219', '78220', 
               '78221', '78222', '78223', '78224', '78225', 
               '78226', '78227', '78228', '78229', '78230', 
               '78231', '78232', '78233', '78234', '78235', 
               '78236', '78237', '78238', '78239', '78240', 
               '78241', '78242', '78243', '78244', '78245', 
               '78246', '78247', '78248', '78249', '78250', 
               '78251', '78252', '78253', '78254', '78255', 
               '78256', '78257', '78258', '78259', '78260', 
               '78261', '78262', '78263', '78264', '78265', 
               '78266', '78268', '78269', '78270', '78275', 
               '78278', '78279', '78280', '78283', '78284', 
               '78285', '78286', '78287', '78288', '78289', 
               '78291', '78292', '78293', '78294', '78295', 
               '78296', '78297', '78298', '78299']

    df = df[df.zip_code.isin(sa_zips)]
    
    # casting open_date as datetime
    df['open_date'] = pd.to_datetime(df['open_date'])
    
    df.to_excel('requests_prepared.xlsx', index=False)

if __name__ == '__main__':

    get_preped_311_data()