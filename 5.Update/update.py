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

# Rename the columns of the small dataset, it changes the names of 
# all columns
theSmall.columns = ["firstName", "lastName", "theEmail"]
# print(theSmall)

# Uppercase the names of all columns
theSmall.columns = [x.upper() for x in theSmall.columns]
# print(theSmall)

# Replace the spaces in each column heading with _
theSmall.columns = theSmall.columns.str.replace(' ','_')

theSmall.rename(columns={'FIRSTNAME': 'first', 'LASTNAME': 'last', 'THEEMAIL': 'email'}, inplace=True)
print(theSmall)

# Rename the headings of columns
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
row2Lastname = theSmall.loc[1][1]
print(row2Lastname)
theSmall.loc[1][1] = 'Smith'
row2Lastname = theSmall.loc[1][1]
print(row2Lastname)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
theSmall.loc[1, ['last']] = 'Anderson'
# print(theSmall.loc[1,['last']])
print(theSmall.loc[1][1])
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
filt = (theSmall['email'] == 'JohnPeters@email.com')
print(theSmall[filt]['last'])
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
theSmall.loc[2][2] == theSmall.loc[2][0]+theSmall.loc[2][1]+'@email.com'
print(theSmall)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# Modify the values of one column
theSmall['email'] = theSmall['email'].str.lower()
print(theSmall)

############ Important data methods ####################
##### 1. APPLY -> never pass args in the function, it's applied on instances
print(theSmall['email'].apply(len))

def updateEmail(email):
    return email.upper()

print(theSmall['first'].apply(updateEmail))

# if we wanted to use a lambda function, you could do
print(theSmall['last'].apply(lambda x: x.lower()))
# print(theSmall)

# returns the len function of each column of the DataFrame
# that means first column has 3 values etc.
# it counts from top to bottom
print(theSmall.apply(len))

# if we wanted to do the same thing on rows, it counts from left
# to right
print(theSmall.apply(len, axis='columns'))

# it retuns a series; each entry represents the first element
# in alphabetic order of its column
print(theSmall.apply(pd.Series.min))

# same with lambda
print(theSmall.apply(lambda  x: x.min()))


###### 2. APPLYMAP -> never pass args in the function, it's applied on instances
# and is used for manipulation of dataframes only not series

# counts the elements of each string (entry)
print(theSmall.applymap(len))

# lowercase all entries
print(theSmall.applymap(str.lower))


###### 3. MAP -> works only on series, substitute a value in a series
# with another value
# it retuns NaN for the values of the series that we haven't substituted
print(theSmall['first'].map({'John': 'Chris', 'Paul': 'Mary'}))

####### 4. Replace 
# it replaces only the selected values
print(theSmall['first'].replace({'John': 'Chris', 'Paul': 'Mary'}))



############### StackOverflow dataset ###############
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# Replace the heading of a column inplace
df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)
print(df['SalaryUSD'])

# The column Hobbyist contains only Yes or No values, so we will use the map 
# method to map the Yes to boolean True and the No to False
# there is not inplace arg for the map method, so we have to assign
# the actual column
df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No': False})
print(df['Hobbyist'])