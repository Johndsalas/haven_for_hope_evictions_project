''' Contains Data for preparing 311 service requests concering homelessness for a Haven for Hope project 

    Out of ~580,000 observations ~3,000 were related to homelessness
    No nulls were found and no modifications to the data were made after removing data not related to homelessness

    Data was last updated on april 20th, 2025.
'''
import pandas as pd

def main():

    # read in data

    df = pd.read_csv('allservicecalls.csv')

    # remove unneeded columns and rename them for clarity

    df = df[['OPENEDDATETIME',
             'Dept', 
             'REASONNAME', 
             'TYPENAME', 
             'OBJECTDESC', 
             'Council District',
             'XCOORD',
             'YCOORD']]


    df = df.rename(columns = {'OPENEDDATETIME' : 'open_date',
                              'Dept' : 'city_dept',
                              'REASONNAME' : 'city_dept_div', 
                              'TYPENAME' : 'type', 
                              'OBJECTDESC' : 'location', 
                              'Council District' : 'council_district',
                              'XCOORD' : 'x_coord',
                              'YCOORD' : 'y_coord'})
    
    # remove rows not related to homelessness

    h_cols = ['Homeless Encampment',
              'Homeless Outreach',
              'Encampment Abatement',
              'Sanitation_Encampment_Abatement',
              'Sanitation_UF-Encampment Abatement',
              'Sanitation_NA-Encampment Abatement']

    df = df[df['type'].isin(h_cols)]

    # write prepared data to csv

    df.to_csv('service_calls_homelessness.csv', index = False)


if __name__ == '__main__':

    main()