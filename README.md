# Haven for Hope Eviction Project

## Goal

The Goal of this project is to investigate whether evictions are a driver of homelessness in San Antonio. I will be measuring evictions using Bexar County court data pertaining to eviction cases in San Antonio and homelessness using 311 service requests pertaining to homelessness in San Antonio.

## Hypothesis

Zip Codes in San Antonio with higher instances of evictions will also show higher instances of homelessness indicating a link between evictions and homelessness.

## Data Dictionary

### SA 311 Homelessness Requests

|Feature|Definition|
|-------|----------|
|open_data| Date request was opened|
|type| Type of request made|
|latitude| Latitudinal coordinate of request|
|longitude| Longitudinal coordinate of request|
|zip_code| Zipcode of request|

### SA Eviction Cases

|Feature|Definition|
|-------|----------|
|case_number| ID number assigned to case|
|judgement_date| Date of most recent decision made on case|
|judgement| Type of decision made most recently on case|
|Zip_code| Zip code where case was ruled|

## Prepare

**311 request data was prepared using the following manner:**
* Relevant columns were renames for ease of use all other columns were dropped
* Dropped rows not pertaining to homelessness
* X and Y coordinate columns were converted from NAD 1983 State Plane Texas South Central FIPS 4204 Feet to Tableau friendly latitude and longitude coordinates using pyproj
* added column of Zip Codes derived from latitude and longitude using geopandas
* Dropped rows with zip codes that were outside of San Antonio

**Bexar County eviction data was prepared using the following manner:**
* Relevant columns were renamed for ease of use all other columns were dropped
* Dropped rows with zip codes that were outside of San Antonio
* Dropped rows with duplicate case numbers keeping only the row with the most recent judgement date for each unique case number
* Dropped rows with disposition value indicating the case did not result in an eviction

**For full preparation details see prep notebooks:**
* [requests_prep_notebook](https://github.com/Johndsalas/haven_for_hope_evictions_project/blob/main/requests_prep_notebook.ipynb)
* [evictions_prep_notebook](https://github.com/Johndsalas/haven_for_hope_evictions_project/blob/main/evictions_prep_notebook.ipynb)

**Prep modules can be found here:**
* [get_requests](https://github.com/Johndsalas/haven_for_hope_evictions_project/blob/main/get_requests.py)
* [get_evictions](https://github.com/Johndsalas/haven_for_hope_evictions_project/blob/main/get_evictions.py)

## Explore

### [Full Exploration Notebook](https://github.com/Johndsalas/haven_for_hope_evictions_project/blob/main/explore.ipynb)

### Is there enough time overlap in the evictions and requests data to make for a good comparison?
* Evictions data cover all of 2024
* Requests data seems to cover from late 2023 to early 2025
* Data will be compared using eviction cases and homelessness requests made during 2024

### What different types of homelessness related 311 requests were made in 2024 and how are they distributed in the data?
* The near totality of requests related to homeless encampments
* A very small portion of requests are for homeless outreach

### Is 311 homelessness requests a good measure of the overall homeless population?
* It stands to reason that a larger homeless population would result in larger and more frequent homeless encampments which would in turn result in a larger number of encampment related requests. For this reason tracking changes in the homeless population using service requests seems reasonable.
* It is unclear how multiple requests regarding the same encampment are tracked or if they are tracked. This may muddy but not enough to discount this as a measure
* Overall I believe that changes in homelessness requests will serve as a good, if imperfect, measure of changes in the homeless population

### What is the distribution of judgements for cases being used to track evictions and are these cases a good measure of total evictions?
* Only cases with judgements for the plaintiff or default judgements were included
* Eviction cases that rule in favor of the plaintiff begin the process of a tenant being evicted
* Default judgements are awarded in the event that one of the parties failing to appear at court. Because the plaintiff would need to file a case for one to exist in the first place it is likely that the grand majority of these cases were in favor of the plaintiff and began an eviction process
* It stands to reason that cases with either judgement as it’s most recent judgement represent an instance of one or more persons being evicted
* Tenants cannot lawfully be evicted in San Antonio without filing for evictions
* For these reasons a change in eviction filings represents a good measure of total number of evictions
* This is not a one for one measure as one eviction case may result in the eviction of more than one tenant from a property

### Is there a correlation between eviction cases and 311 homelessness requests?
* Information from the requests and eviction data was combined to gather the number of homelessness requests and eviction cases per zip code in San Antonio in 2024
* A scatterplot and correlation test of homelessness requests and eviction cases by zip code shows a strong correlation between the two that is statistically significant

## Visualizations
* A heatmap of eviction cases by zip code overlayed by a measles map of homelessness requests has been produced in Tableau to further explore the relationship between eviction cases and 311 homelessness requests.
* A scatterplot of the number of eviction cases and homelessness requests occuring in the same zip code has been made to explore the correlation between the two.

## Conclusion
* Fluxuations in the number of 311 calls related to homelessness seem to be a good indicator of fluctuations in the homeless population
* Fluxuations in the number of eviction cases with judgements likely leading to evictions seems to be a good indicator of fluctuations in the total number of evictions
* There is a strong correlation between the number of eviction cases and the number of 311 calls related to homelessness in San Antonio in 2024
* This suggests a link between evictions and homelessness
* All available evidence suggests that evictions is a driver of homelessness

## Further Inquiry
* Because the evidence we have is correlatory we cannot rule out the possibility that evictions and homelessness are both independently driven by third variable such as population
* More research into this possibility should be conducted in the future
