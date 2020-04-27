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

# median value on a series
print(df['ConvertedComp'].median())

# look over the entire dataframe, find the columns which contain numerical
# values and calculate the median of each one
print(df.median())

# returns the statistical description of the numerical columns of 
# our dataframe
print(df.describe())

# return the number of numerical values in a column
print(df['ConvertedComp'].count())

# retuns the number of each category in the column
print(df['Hobbyist'].value_counts())

# returns the percentages of each category in the column
print(df['SocialMedia'].value_counts(normalize=True))

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
##################### GROUPING #####################

# set up a filter depending on 1 column, and get the group (new dataframe) whose
# entry in the 1 column is given by us
countryGroup = df.groupby(['Country'])
print(countryGroup.get_group('United States'))
print(countryGroup['SocialMedia'].value_counts(normalize=True).loc['Greece'])

# another way to do the above
filt = df['Country'] == 'Greece'
print(df.loc[filt]['SocialMedia'].value_counts())

# Note: The first method is preferred in data analysis, because we 
# do not need to apply a filter to each country (column)

# Find the median salary in Germany
print(countryGroup['ConvertedComp'].median().loc['Germany'])

# Work with aggregate functions
print(countryGroup['ConvertedComp'].agg(['median', 'mean']).loc['Canada'])

# How many people said that they know Python in the survey
# using filtering
filt = df['Country'] == 'India'
print(df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum())
# using actual pandas
# what % of people from each country know Python?
print(countryGroup['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').value_counts(normalize=True)))

# another way
country_respondents = df['Country'].value_counts()
country_uses_python = countryGroup['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
python_df = pd.concat([country_respondents, country_uses_python], axis='columns', sort=False)
python_df.rename(columns={'Country': 'NumRespondents', 'LanguageWorkedWith': 'NumKnowsPython'}, inplace=True)
python_df['PctKnowsPython'] = (python_df['NumKnowsPython']/python_df['NumRespondents']) * 100
python_df.sort_values(by='PctKnowsPython', ascending=False, inplace=True)
print(python_df.loc['Greece'])