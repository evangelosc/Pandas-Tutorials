#!/Users/evan/env/bin/python

import pandas as pd
df = pd.read_csv('./../ourData/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('./../ourData/survey_results_schema.csv', index_col='Column')
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# We check if all entries in the QuestionText col are equal to 'Hobbyist',
# it retruns T or F. It does not work with the index col
print(schema_df['QuestionText'] == 'Hobbyist')

# Useful convertions
import numpy as np
x = np.array(schema_df['QuestionText'] == 'Hobbyist')
print(x.tolist())
print(x)


# A way of filtering, it returns the new dataset where the condition is True
# We do not have a specific match, so it does not return anything
print(schema_df[x])

# The & and | operators can be used for filtering in terms of logical 
# AND and OR respectively.
# for example:
#     schema_df[x & schema_df['QuestionText'] == 'Teacher']

# Furthemore, the ~ operator can be used for logical NOT.



countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']
filt = df['Country'].isin(countries)
print(df.loc[filt, 'Country'])


highSalary = (df['ConvertedComp'] > 70000)
print(df.loc[highSalary, ['Country', "LanguageWorkedWith", 'ConvertedComp']])

# Filter String Methods
# Na=False ignores the not a numbers
theFilter = df['LanguageWorkedWith'].str.contains('Python', na=False)
print(df.loc[theFilter, 'LanguageWorkedWith'])