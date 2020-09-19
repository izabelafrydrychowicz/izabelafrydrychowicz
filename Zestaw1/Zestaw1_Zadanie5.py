#Selected columns: Age, YearsCodePro

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

df_schema = pd.read_csv('survey_results_schema.csv')
df_survey = pd.read_csv('survey_results_public.csv', usecols=['Respondent', 'Age', 'YearsCodePro'],
                        index_col='Respondent')

#Check types of objects in df_survey dataframe.
type_obj=df_survey.dtypes

#Remove missing values.
df_survey.dropna(inplace=True)


#Return the flattened underlying data as an ndarray.
column_values = df_survey[['Age']].values.ravel()
#Return uniques in order of appearance.
unique_values = np.unique(column_values)

column_values = df_survey[['YearsCodePro']].values
unique_values = np.unique(column_values)
df_survey.replace(to_replace={'Less than 1 year': '0',
                              'More than 50 years': '51'},
                  inplace=True)

#Change type from float to int.
df_survey = df_survey.astype('int64', copy=False)

#First plot.

plt.plot(df_survey['Age'],df_survey['YearsCodePro'],'ro', markersize=0.3)
plt.title('Years coded professionally depending on age')
plt.xlabel('Age')
plt.ylabel('Years coded professionally')
plt.show()

#Second plot.

df_survey_two=pd.read_csv('survey_results_public.csv', usecols=['Respondent', 'Age', 'YearsCodePro','Gender'],
                        index_col='Respondent')

#Add column Gender to df_survey.
df_survey['Gender']=df_survey_two['Gender']

#Prepare the data for the male chart
only_men=df_survey['Gender']=='Man'
df_survey_men=df_survey[only_men]
#print(df_survey_men.head(20))

#Prepare the data for the female chart
only_women=df_survey['Gender']=='Woman'
df_survey_women=df_survey[only_women]
#print(df_survey_women.head(20))

#Chart for men
plt.plot(df_survey_men['Age'],df_survey_men['YearsCodePro'],'ro', markersize=0.3)
plt.title('Years coded professionally depending on age - MEN')
plt.xlabel('Age')
plt.ylabel('Years coded professionally')
plt.show()

#Chart for women
plt.plot(df_survey_women['Age'],df_survey_women['YearsCodePro'],'ro', markersize=0.3)
plt.title('Years coded professionally depending on age - WOMEN')
plt.xlabel('Age')
plt.ylabel('Years coded professionally')
plt.show()