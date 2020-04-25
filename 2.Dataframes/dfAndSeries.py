#!/Users/evan/env/bin/python

import pandas as pd
df = pd.read_csv('./../ourData/survey_results_public.csv')
schema_df = pd.read_csv('./../ourData/survey_results_schema.csv')
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
print(df.SurveyLength) # Dot notation for printing a col
print(df['SurveyLength']) # Brackets notation for printing a col

print(df[['SurveyLength', 'SurveyEase']]) # pass a list of elements for printing the cols of them

print(df.columns)

print(df.iloc[0]) # prints the first row
print(df.iloc[[0,1]]) # pass a list of elements and prints the rows of them

print(df.iloc[[0, 1], 2]) # prints the first two rows of the second col
print(df.loc[[0,1],['SurveyLength', 'SurveyEase']]) # prints the first two rows of the given cols (second list)