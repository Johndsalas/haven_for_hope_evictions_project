# Haven for Hope Eviction Project

## Goal 

The Goal of this project is to investigate whether evictions are a driver of homelessness in San Antonio. I will be measuring evictions using Bexar County court data pertaining to eviction cases in San Antonio and homelessness using 311 service requests pertaining to homelessness in San Antonio. 

 ## Hypothesis 

Zip Codes in San Antonio with higher instances of evictions will also show higher instances of homelessness indicating a link between evictions and homelessness.

## Data Dictionary 

## Preparation 

**311 request data was prepared using the following manner:**
* Relevant columns were renames for ease of use all other columns were dropped
*  Dropped rows not pertaining to homelessness
* X and Y coordinate columns were converted from NAD 1983 State Plane Texas South Central FIPS 4204 Feet to Tableau friendly latitude and longitude coordinates using pyproj
* added column of Zip Codes derived from latitude and longitude using geopandas
* Dropped rows with zip codes that were outside of San Antonio

**Bexar County eviction data was prepared using the following manner:**
* Relevant columns were renames for ease of use all other columns were dropped
* Dropped rows with zip codes that were outside of San Antonio
* Dropped rows with duplicate case numbers keeping only the row with the most recent judgement date for each unique case number
* Dropped rows if disposition value indicates the case did not result in an eviction

For full preparation details see prep notebooks:
* 311 homelessness requests
* Bexar county evictions

