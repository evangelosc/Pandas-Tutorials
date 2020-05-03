import pandas as pd
import numpy as np

people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}

df = pd.DataFrame(people)
print(df)
 
# it drops the rows of missing values
# if it was set to all, it would have removed the rows with
# all missing values
print(df.dropna(axis='index', how='any', subset=['email']))


df.replace('NA', np.nan, inplace=True)
df.replace('Missing', np.nan, inplace=True)

df.isna()
df.fillna(0)
df['age'] = df['age'].astype(float)
df['age'].mean()

df = pd.read_csv('./../ourData/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('./../ourData/survey_results_schema.csv', index_col='Column')
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df['YearsCode'].head(10)
df['YearsCode'].unique()
df['YearsCode'].replace('Less than 1 year', 0, inplace=True)
df['YearsCode'].replace('More than 50 years', 51, inplace=True)
df['YearsCode'] = df['YearsCode'].astype(float)
df['YearsCode'].mean()
df['YearsCode'].median()
