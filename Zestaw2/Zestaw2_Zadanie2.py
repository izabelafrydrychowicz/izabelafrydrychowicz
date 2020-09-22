import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

# Read file and create a dataframe.
df = pd.read_csv("survey_results_public.csv", header=0,
                 usecols=['WorkWeekHrs', 'CompTotal', 'YearsCode', 'Age', 'Age1stCode','BetterLife','Gender'])

# Remove missing values.
df = df.dropna()

df.loc[df['YearsCode'] == 'Less than 1 year'] = 0
df.loc[df['YearsCode'] == 'More than 50 years'] = 51
df.loc[df['Age1stCode'] == 'Younger than 5 years'] = 0
df.loc[df['Age1stCode'] == 'Older than 85'] = 86
df['YearsCode'] = df['YearsCode'].astype("float64")
df['Age1stCode'] = df['Age1stCode'].astype('float64')
df['Gender'] = df['Gender'].astype('str')

# Check types of objects in df dataframe.
type_obj = df.dtypes

# Numeric data instead of yes / no -> 'map' function ssed for substituting each value in a Series with another value.
map_values = {'Yes': 1, 'No': 0}
df['BetterLife'] = df['BetterLife'].map(map_values)

# Create a One-Hot encoding variable
# 'isin' - whether each element in the DataFrame is contained in values.
df = df[df['Gender'].isin(['Woman', 'Man'])]
df = pd.get_dummies(df, columns=['Gender'])
