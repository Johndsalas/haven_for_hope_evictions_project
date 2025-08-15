''' Contains code for preparing evictions data'''

import pandas as pd

def get_prepared_eviction_data():
    '''Prepare eviction data for project'''
    
    # read in unprepared data
    df = pd.read_excel('eviction_cases.xlsx')

    # get relevent columns and rename for ease of use
    df = drop_and_rename(df)

    # get 5 digit zip codes and drop rows that have zip codes that are not in San Antonio
    df = get_sa_zips(df)

    # drop rows with duplicate case numbers keeping only the most recent
    df = drop_duplicate_case_numbers(df)

    # drop rows where disposition is not likely to result in eviction
    df = get_evictions(df)

    # export df to excel file
    df.to_excel('evictions_full_prep.xlsx', index=False)


def drop_and_rename(df):
    '''Take in a dataframe 
       Rename relevent columns for ease of use drop other columns
       Return dataframe'''
    
    # get relevant columns and rename for clarity
    df = df[['CaseNumber',        # used to distinguish unique cases
             'JUDGMENT_DT',       # used for date case was ruled on
             'POSTAL_CD',         # used for zip code
             'Disposition']]      # used to determine result of case


    df = df.rename(columns={'CaseNumber'      : 'case_number',
                            'JUDGMENT_DT'     : 'judgement_date',
                            'POSTAL_CD'       : 'zip_code',
                            'Disposition'     : 'disposition'})
    
    return df


def get_sa_zips(df):
    '''Take in a dataframe 
       get 5 digit zip codes and drop rows that have zip codes that are not in San Antonio
       Return dataframe'''
    
    # drop rows with zip codes not in San Antonio
    # get first five digits of values in zip_code column
    df['zip_code'] = df.zip_code.apply(lambda x : str(x)[:5])

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

    # keep only rows that have a zip code in sa_zips
    df = df[df.zip_code.isin(sa_zips)]
    
    return df


def drop_duplicate_case_numbers(df):
    '''Take in a dataframe 
       drop rows with duplicate case numbers keeping only the most recent
       Return dataframe'''
    
    # drop rows with duplicate case numbers
    # sort values in descending order
    df = df.sort_values(by='judgement_date',ascending=False).reset_index(drop=True)

    # drop rows with duplicate case numbers keeping only the first
    df = df.drop_duplicates(subset='case_number', keep='first').reset_index(drop=True)

    return df


def  get_evictions(df):
    '''Take in a dataframe 
       drop rows where disposition is not likely to result in eviction
       Return dataframe'''
    
    # drop rows where disposition is not likely to result in eviction
    evict = ['Default Judgments (OCA)',
             'Judgment for Plaintiff (OCA)']

    df = df[df.disposition.isin(evict)]

    return df
    

if __name__ == '__main__':

    get_prepared_eviction_data()