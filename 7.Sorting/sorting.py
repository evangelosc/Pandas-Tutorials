#!/Users/evan/env/bin/python

import pandas as pd
df = pd.read_csv('./../../ourData/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('./../../ourData/survey_results_schema.csv', index_col='Column')
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

small_df = {
    "first": ["Nick", "Paul", "John"],
    "last": ["Wallace", "Richardson", "Peters"],
    "email": ["NickWallace@email.com", "PaulRichardson@email.com", "JohnPeters@email.com"]
}
theSmall = pd.DataFrame(small_df)

# sort the values depending on lastnames, if we want the sorting in
# descending order, we equal ascending to false
theSmall = theSmall.sort_values(by='last', ascending=False)
print(theSmall)

# If there are dublicates in the last col, we can specify a second
# column for sorting
theSmall = theSmall.sort_values(by=['last', 'first'], ascending=False)
print(theSmall)

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# IF there are dublicates in the last col, we can specify a second 
# column for sorting and change the hierarchy to ascending for the
# second column
theSmall.sort_values(by=['last', 'first'], ascending=['False', 'True'], inplace=True)
print(theSmall)

# If we want to sort depending on the index
theSmall.sort_index()
print(theSmall)






print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# sort by ascending order of countries and descending of ConvertedComp
df.sort_values(by=['Country', 'ConvertedComp'], ascending = [True, False], inplace=True)
print(df[['Country','ConvertedComp']].head(50))

# print the 10 largest salaries
print(df['ConvertedComp'].nlargest(10))

# see also other columns
print(df.nlargest(10, 'ConvertedComp'))