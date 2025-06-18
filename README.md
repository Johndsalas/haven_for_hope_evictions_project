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

## Preparation

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
* (311 homelessness requests)[Add Link]
* (Bexar county evictions)[Add Link]

**Prep modules can be found here:**
* (prepare_sa_311_homelessness_requests.py)[Add Link]
* (prepare_sa_eviction_cases.py)[Add Link]

## Exploration

Exploration of the data centers on these questions.
1) what is the time overlap between the requests data and the eviction data?
2) What types of homeless related 311 request are being made and what is the distribution during that time?
3) Of the types of judgements likely to result in evictions what are those type and what is the distribution during that time?
4) Is there a correlation between the number of eviction cases and homelessness cases in a given zip code during that time?
* See (exploration.ipynb)[Add Link] for full exploratory analysis

## Visualizations
* A heatmap of eviction cases by zip code overlayed by a measles map of homelessness requests has been produced in Tableau to further explore the relationship between eviction cases and 311 homelessness requests.
* A scatterplot of the number of eviction cases and homelessness requests occuring in the same zip code has been made to explore the correlation between the two.

## Conclusion
