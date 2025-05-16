''' Contains code for preparing evictions data'''

import pandas as pd
from thefuzz import fuzz

import warnings
warnings.filterwarnings("ignore")


def get_prepared_eviction_data():
    '''Prepare eviction data for project'''
    
    # read in unprepared data
    df = pd.read_excel('evictions_2023.xlsx')
    
    # get relevant columns and rename for clarity
    df = df[['CaseNumber',        # used to distinguish unique cases
             'CaseFileDate',      # used for case date
             'JUDGMENT_DT',       # used for date case was ruled on
             'DispositionDate',   # used for date of disposition
             'CITY_NAME',         # used for city location
             'POSTAL_CD',         # used for zip code
             'Disposition',        # used to determine if case was dismissed
             ]]   

    df = df.rename(columns={'CaseNumber'      : 'case_number',
                            'CaseFileDate'    : 'file_date',
                            'JUDGMENT_DT'     : 'judgement_date',
                            'DispositionDate' : 'disposition_date',
                            'CITY_NAME'       : 'city',
                            'POSTAL_CD'       : 'zip_code',
                            'Disposition'     : 'disposition'})
    
    # adjust values in cities for misspellings of san antonio
    df['city'] = df.city.apply(fuzzy_sa)

    # remove cities not in list of acceptaple cities
    cities = ['san antonio']

    df = df[df.city.isin(cities)]

    # get first five digits of values in zip_code column
    df['zip_code'] = df.zip_code.apply(lambda x : str(x)[:5])

    # remove duplicate case numbers keeping the latest according to the disposition date
    df = df.sort_values(by='disposition_date',ascending=False).reset_index(drop=True)

    df = df.drop_duplicates(subset='case_number', keep='first').reset_index(drop=True)
    
    # removing rows where disposition is not likely to result in eviction
    evict = ['Default Judgments (OCA)',
             'Judgment for Plaintiff (OCA)']

    df = df[df.disposition.isin(evict)]
    
    # remove columns used for filtering
    df = df[['case_number',
             'disposition_date',
             'zip_code']].reset_index(drop=True)
    
    df.to_excel('evictions_prepared.xlsx')
    
    
def fuzzy_sa(value):
    ''' takes in a pandas value and returns san antonio if string is a 90 or higher ratio to san antonio
        otherwise returns lower cased version of the original string'''
    
    value = str(value).lower()
    
    sa1 = 'san antonio'
    sa2 = 'sa'
    
    ratio1 = fuzz.ratio(sa1,value)
    ratio2 = fuzz.ratio(sa2,value)
    
    if (ratio1 >= 80) or (ratio2 >= 60):
        
        return 'san antonio'
    
    else:
        
        return value
    

if __name__ == '__main__':

    get_prepared_eviction_data()