# AdevintaPatriciaCarmona
This report was created using Python and pandas analysis. Main codding activity was developed in a Jupyter Notebook, where you can find:

1. Data Exploration
2. CTR calculation
3. Zero rate calculation
4. Results people tend to try [incomplete]
5. Sessions lengths calculation [incomplete]


## Data Exploration

First, data analysis with pandas helped to know better type of data, how many registers there were, if there were null values, etc.

Based on this info, main KPI's were defined: clicks to calculate CTR and Zero results. 

## CTR Calculation

At the begginning, I found that checkin serie could help with clicks thanks to the tag "visitPage". Every register tagged as "visitPage" was considered a click. The first attempt was manually, but later I developed a function (>> src/rates) to know which was the overall CTR for those days. Later I created a dataframe to store results day by day and group by group. 

**Issue with timestamp.** This took some time to know that timestamp had 16 units as was causing a problem when casting to datetime because it only considers 14 units. I round to those and then cast to datetime to get each day.

**Group by day.** Once timestamp series was casted, I used resample method to group by day and get CTR daily.