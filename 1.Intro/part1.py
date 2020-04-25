#!/Users/evan/env/bin/python

import pandas as pd
import numpy as np
df = pd.read_csv('./../ourData/survey_results_public.csv')
print(df.shape) # returns (rows x col)
print(df.info) # not really important


# best use with jyputer notebooks; it displays all the cols
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

schema_df = pd.read_csv('./../ourData/survey_results_schema.csv')
print(schema_df)
print(schema_df.head(10)) # shows only the first 10 rows
print(schema_df.tail(10)) # shows only the last 10 rows