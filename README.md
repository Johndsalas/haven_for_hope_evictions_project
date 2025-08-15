# Haven for Hope Eviction Project

## Goal

Explore the relationship between evictions and homelessness, as measured by eviction cases and 311 service requests occurring in San Antonio in 2024, by evaluating their statistical relationship and visualizing their geospatial relationship

## Research Questions

1) What is the statistical relationship between eviction cases and 311 service calls for homelessness related issues?
2) What is the geospatial relationship between eviction cases and 311 service calls?

## Prepare

Data was gathered and prepared for initial exploration using the following methods

**311 request data was prepared using the following manner:**
* The original data was downloaded from [Open Data SA](https://data.sanantonio.gov/dataset/service-calls)
* Relevant columns were renames for ease of use all other columns were dropped
* Dropped rows not pertaining to homelessness
* X and Y coordinate columns were converted from NAD 1983 State Plane Texas South Central FIPS 4204 Feet to Tableau friendly latitude and longitude coordinates using pyproj
* added column of Zip Codes derived from latitude and longitude using geopandas
* Dropped rows with zip codes that were outside of San Antonio
* When exploration notebook is run it produces an additional export of the data containing only data from 2024

**Bexar County eviction data was prepared using the following manner:**
* The original data was provided by Bexar County to Ryan Orsinger, Director of Data Science and Research at Haven for Hope, who provided the data to me
* Relevant columns were renamed for ease of use all other columns were dropped
* Dropped rows with zip codes that were outside of San Antonio
* Dropped rows with duplicate case numbers keeping only the row with the most recent judgement date for each unique case number
* Dropped rows with disposition value indicating the case did not result in an eviction

## Data Dictionary

During preparation data was modified to contain the following

### SA Eviction Cases

|Feature|Definition|
|-------|----------|
|case_number| ID number assigned to case|
|judgement_date| Date of most recent decision made on case|
|judgement| Type of decision made most recently on case|
|Zip_code| Zip code where case was ruled|

### SA 311 Homelessness Requests

|Feature|Definition|
|-------|----------|
|open_data| Date request was opened|
|type| Type of request made|
|latitude| Latitudinal coordinate of request|
|longitude| Longitudinal coordinate of request|
|zip_code| Zipcode of request|

**For full preparation details see prep notebooks:**
* [evictions_prep_notebook](https://github.com/Johndsalas/haven_for_hope_evictions_project/blob/main/evictions_prep_notebook.ipynb)
* [requests_prep_notebook](https://github.com/Johndsalas/haven_for_hope_evictions_project/blob/main/requests_prep_notebook.ipynb)

## Notebook Exploration Key Questions and Findings

### Is there enough time overlap in the evictions and requests data to make for a good comparison?
* Evictions data cover all of 2024
* Requests data seems to cover from late 2023 to early 2025
* Data can be compared using eviction and request data collected for 2024

### What different types of homelessness related 311 requests were made in 2024 and how are they distributed in the data?
* The near totality of requests related to homeless encampments
* A very small portion of requests are for homeless outreach

### Are 311 homelessness requests a good measure of the overall homeless population?
* It stands to reason that a larger homeless population would result in larger and more frequent homeless encampments which would in turn result in a larger number of encampment related 311 requests. For this reason tracking changes in the homeless population using these requests seems reasonable.
* It is unclear how multiple requests regarding the same encampment are tracked or if they are tracked. This may muddy the results but not enough to discount this as a measure
* Overall I believe that changes in homelessness requests will serve as a good, if imperfect, measure of changes in the homeless population

### What is the distribution of judgements for cases being used to track evictions and are these cases a good measure of total evictions?
* Only cases with judgements for the plaintiff or default judgements were included
* Eviction cases that rule in favor of the plaintiff begin the process of a tenant being evicted
* Default judgements are awarded in the event that one of the parties failing to appear at court. Because the plaintiff would need to file a case for one to exist in the first place it is likely that the grand majority of these cases were in favor of the plaintiff and began an eviction process
* It stands to reason that cases with either judgement as it’s most recent judgement represent an instance of one or more persons being evicted
* Tenants cannot lawfully be evicted in San Antonio without filing for evictions
* Informal evictions such as those between family members may not go through a formal eviction process and so will not appear in our data
* While we cannot capture all evictions in our data it stands to reason that changes in eviction case numbers will, if imperfectly, reflect changes in the total number of evictions so it is a good measure to use

### Is there a correlation between eviction cases and 311 homelessness requests?
* Information from the requests and eviction data was combined to gather the number of homelessness requests and eviction cases per zip code in San Antonio in 2024
* A scatterplot and correlation test of this shows a strong correlation between the two that is statistically significant

### Notebook Exploration Conclusions
* Fluxuations in the number of 311 calls related to homelessness seem to be a good indicator of fluctuations in the homeless population
* Fluxuations in the number of eviction cases with judgements likely leading to evictions seem to be a good indicator of fluctuations in the total number of evictions
* There is a strong correlation between the number of eviction cases and the number of 311 calls related to homelessness in San Antonio in 2024
* All available evidence suggests that evictions is a driver of homelessness

### [Exploration Notebook](https://github.com/Johndsalas/haven_for_hope_evictions_project/blob/main/explore.ipynb)

## Reproducibility

The following modules can be used to modify data from its original form to project ready. Including modifying service request data to only include data from 2024. Your project folder must include a copy of the original data and any supplemental files needed for all utilized python libraries.

* [get_requests](https://github.com/Johndsalas/haven_for_hope_evictions_project/blob/main/get_requests.py)
* [get_evictions](https://github.com/Johndsalas/haven_for_hope_evictions_project/blob/main/get_evictions.py)

This module can be used to combine the prepared version of each data into a dataframe that contains the number of eviction cases and 311 service requests occured in each San Antonio zip code in 2024

* [get_zip_compare](copythelinkwhenyoumakethemodule)

## Tableau Exploration

The original goal and research questions are explored, as well as observations and conclusions presented in a Tableau story

### [Full Tableau Story](https://public.tableau.com/app/profile/john.salas/viz/HavenEvictionsProject/Story?publish=yes)

## Further Inquiry
* Because the evidence we have is correlatory we cannot rule out the possibility that evictions and homelessness are both independently driven by third variable such as population
* More research into this possibility should be conducted in the future
