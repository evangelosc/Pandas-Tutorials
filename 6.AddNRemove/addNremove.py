#!/Users/evan/env/bin/python

import pandas as pd
df = pd.read_csv('./../ourData/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('./../ourData/survey_results_schema.csv', index_col='Column')
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

small_df = {
    "first": ["Nick", "Paul", "John"],
    "last": ["Wallace", "Richardson", "Peters"],
    "email": ["NickWallace@email.com", "PaulRichardson@email.com", "JohnPeters@email.com"]
}
theSmall = pd.DataFrame(small_df)
# print(theSmall)

# Add a Fullname Column
theSmall['fullname'] = theSmall['first'] + ' ' + theSmall['last']
print(theSmall)

# It replaces the value of each entry of the first column to None
theSmall['first'] = None
print(theSmall)

# drops out the first column
theSmall.drop(columns=['first', 'last'], inplace=True)
print(theSmall)

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# Retrieve from fullname column the first and last names columns
# print(theSmall['fullname'].str.split(' ', expand=True))
theSmall[['first', 'last']] = theSmall['fullname'].str.split(' ', expand=True)
print(theSmall)

# swap columns in the dataframe
thelist = list(theSmall)
thelist[0], thelist[2] = thelist[2], thelist[0]
theSmall.columns = thelist
print(theSmall)

colTitles = ['first', 'last', 'fullname', 'email']
theSmall = theSmall.reindex(columns=colTitles)
print(theSmall)

small_df = {
    "first": ["Nick", "Paul", "John"],
    "last": ["Wallace", "Richardson", "Peters"],
    "email": ["NickWallace@email.com", "PaulRichardson@email.com", "JohnPeters@email.com"]
}
theSmall = pd.DataFrame(small_df)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(theSmall)
# Add a single row of data, we do not need to define a new dataframe
# because it's one row long
theSmall = theSmall.append({'first': 'Tony', 'last':'Charlesson'}, ignore_index=True)
print(theSmall)

# Append a smaller dataframe to our main dataframe
smaller = {
    "first": ["Tony", "Steve"],
    "last": ["Stark", "Rogers"],
    "email": ["TonyStark@email.com", "SteveRogers@email.com"]
}
theS = pd.DataFrame(smaller)
theSmall = theSmall.append(theS, ignore_index=True, sort=False)
print(theSmall)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# Remove an entire row from the dataset depending on one condition
theSmall = theSmall.drop(index=theSmall[theSmall['last'] == 'Richardson'].index)
print(theSmall)