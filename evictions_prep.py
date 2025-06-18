''' Contains code for preparing evictions data'''

import pandas as pd

def get_prepared_eviction_data():
    '''Prepare eviction data for project'''
    
    # read in unprepared data
    df = pd.read_excel('evictions_2023.xlsx')
    
    # get relevant columns and rename for clarity
    df = df[['CaseNumber',        # used to distinguish unique cases
             'JUDGMENT_DT',       # used for date case was ruled on
             'POSTAL_CD',         # used for zip code
             'Disposition']]      # used to determine result of case


    df = df.rename(columns={'CaseNumber'      : 'case_number',
                            'JUDGMENT_DT'     : 'judgement_date',
                            'POSTAL_CD'       : 'zips',
                            'Disposition'     : 'disposition'})

    # drop rows with zip codes not in
    # get first five digits of values in zip_code column
    df['zips'] = df.zips.apply(lambda x : str(x)[:5])

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
    df = df[df.zips.isin(sa_zips)]
    
    # drop rows with duplicate case numbers
    # sort values in descending order
    df = df.sort_values(by='judgement_date',ascending=False).reset_index(drop=True)

    # drop rows with duplicate case numbers keeping only the first
    df = df.drop_duplicates(subset='case_number', keep='first').reset_index(drop=True)

    # drop rows where disposition is not likely to result in eviction
    evict = ['Default Judgments (OCA)',
             'Judgment for Plaintiff (OCA)']

    df = df[df.disposition.isin(evict)]
    
    df.to_excel('evictions_prep.xlsx')
    

if __name__ == '__main__':

    get_prepared_eviction_data()