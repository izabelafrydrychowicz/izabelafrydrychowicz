#Selected columns: Age, YearsCodePro

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

df_schema = pd.read_csv('survey_results_schema.csv')
df_survey = pd.read_csv('survey_results_public.csv', usecols=['Respondent', 'Age', 'YearsCodePro'],
                        index_col='Respondent')

#Check types of objects in df_survey dataframe.
type_obj=df_survey.dtypes
print(type_obj)
#Show 20 rows.
print(df_survey.head(20))
#Check amount of columns and amount of rows.
print(df_survey.shape)
#Remove missing values.
df_survey.dropna(inplace=True)
print(df_survey.shape)
print(df_survey.dtypes)
#Print information about a DataFrame including the index dtype and columns, non-null values and memory usage
print(df_survey.info())

#Return the flattened underlying data as an ndarray.
column_values = df_survey[['Age']].values.ravel()
#Return uniques in order of appearance.
unique_values = np.unique(column_values)
print(unique_values)

column_values = df_survey[['YearsCodePro']].values
unique_values = np.unique(column_values)
print(unique_values)
df_survey.replace(to_replace={'Less than 1 year': '0',
                              'More than 50 years': '51'},
                  inplace=True)

#Change type from float to int.
df_survey = df_survey.astype('int64', copy=False)

#Check type of data.
print(df_survey.dtypes)

