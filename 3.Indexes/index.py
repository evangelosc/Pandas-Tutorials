#!/Users/evan/env/bin/python

import pandas as pd
df = pd.read_csv('./../ourData/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('./../ourData/survey_results_schema.csv', index_col='Column')
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)



#######     rule of thumb   ###########
# if inplace is True:
#     no need to assign
# else:
#     assign

# it creates a new dataframe, which is indexed by the Ethnicity col
# if we pass another argument inplace=True, it modifies the current dataframe
print(df.set_index('Ethnicity'))
df.set_index('Ethnicity', inplace=True)
# print(df)
# print(df.index)

# if we have modified the index of our dataframe inplace,
# we can run the following in order to set up as initially
df.reset_index(inplace=True)


# returns the question, which is associated with the hobbyist.
# that happens because we have indexed the schema_df depending on the Column col
# so ['Hobbyist'] returns its entire row
print(schema_df.loc['Hobbyist'])

# My terminal truncates the question under the MgrIdiot and does not show it entirely
# if I pass as second argument to the loc the name of col, that MgrIdiot
# resides, it shows the actual output
print(schema_df.loc['MgrIdiot', 'QuestionText'])

# It sort inplace the dataframe depending on the index col and in 
# descending order
schema_df.sort_index(inplace=True, ascending=False)
print(schema_df)