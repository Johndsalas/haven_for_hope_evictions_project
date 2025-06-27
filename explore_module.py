'''                                                 Holds background code for exploration notebook                          '''

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# import data sets

def time_stamp(edf,rdf):
    '''Prints time stamp information for evictions and requests data
       exports requests data to excel shortened to only include data 
       from 2024'''

    print(f'The eviction dataframe contains data from') 
    print(f'{edf.judgement_date.min()}')
    print(f'to') 
    print(f'{edf.judgement_date.max()}')
    print()
    print(f'The requests dataframe contains data from') 
    print(f'{rdf.open_date.min()}')
    print(f'to') 
    print(f'{rdf.open_date.max()}')
    print()
    print("Trimming request data to include only 2024")
    print('exporting to requests_2024')
    # modifying request data to include only 2024 data 
    rdf = rdf[rdf['open_date'].dt.year == 2024]

    rdf.to_excel('requests_2024.xlsx')

    return rdf


def get_request_bar(rdf):
    ''' Prints bar graph of type column from requests dataframe'''

    colors = ['lightblue', 'lightblue','darkgrey','lightblue','lightblue','lightblue']

    plt.figure(figsize=(10, 6))
    rdf.type.value_counts().plot(kind='bar', color = colors)
    plt.title("Overwelming Majority of Requests are for Homeless Encampments")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Count')
    plt.plot()


def get_case_bar(edf):
    '''Prints bar graph of disposition column of evictions dataframe'''

    plt.figure(figsize=(10, 6))
    edf.disposition.value_counts().plot(kind='bar', color = 'lightblue')
    plt.title("Only Default judgements or Judgements for the Plaintiff are Considered")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Count')
    plt.plot()


def get_zip_compare(edf,rdf):
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
    zipdf = pd.DataFrame(zip_dict)

    zipdf.to_excel('compare_zips_2024.xlsx')
        
    return zipdf, rdf, edf


def get_zip_scatter(zipdf):
    '''Prints a scatterplot or eviction cases and homelessness requests found in zipdf 
       along with correlation coefficient and p-value'''
    
    # graph info
    zipdf.plot.scatter(x='eviction_cases', y='homelessness_requests')
    plt.title('Strong Correlation Between Eviction Cases and Homelessness Requests')
    plt.xlabel('Eviction Cases')
    plt.ylabel('Homelessness Requests')
    plt.grid(True)
    plt.show()

    # get and print correlation coefficient and p-value
    correlation_coeff, p_value = pearsonr(zipdf['eviction_cases'], zipdf['homelessness_requests'])
    
    print(f'Correlation Coefficient: {correlation_coeff}')
    print(f'P-value: {p_value}')
    
