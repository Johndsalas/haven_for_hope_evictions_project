''' Module for preparing a dataframe comparing the number of eviction cases and service calls per zip code using data prepared for this project'''

import pandas as pd

def get_zip_compare():
    '''Takes in evictions and requests dataframes
       Returns both dataframes with zipcode column set to string type
       and a dataframe showing the number of homelessness requests and eviction
       cases took place in each zipcode in San Antonio in 2024'''
    
    

    # cast zip_code column in both df's as string type
    rdf['zip_code'] = rdf.zip_code.astype(str)
    edf['zip_code'] = edf.zip_code.astype(str)

    # empty dict
    zip_dict = {'zip_code':[],
                'homelessness_requests':[],
                'eviction_cases':[]}

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

    # adding information to dict
    for item in sa_zips:
        
        zip_code = item
        
        recs = len(rdf[rdf.zip_code == zip_code])
        
        evicts = len(edf[edf.zip_code == zip_code])
        
        li =[zip_code, recs, evicts]
        
        for i, key in enumerate(zip_dict):
            
            zip_dict[key].append(li[i])

    # converting dict to dataframe
    df = pd.DataFrame(zip_dict)

    df.to_excel('zip_zips_2024.xlsx')
        
    return df