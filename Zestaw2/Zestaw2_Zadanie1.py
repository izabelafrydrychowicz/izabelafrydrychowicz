import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read file and create a dataframe.
df = pd.read_csv("survey_results_public.csv", header=0,
                 usecols=['WorkWeekHrs', 'CompTotal', 'YearsCode', 'Age', 'Age1stCode'])

# Remove missing values.
df = df.dropna()

df.loc[df['YearsCode'] == 'Less than 1 year'] = 0
df.loc[df['YearsCode'] == 'More than 50 years'] = 51
df.loc[df['Age1stCode'] == 'Younger than 5 years'] = 0
df.loc[df['Age1stCode'] == 'Older than 85'] = 86
df['YearsCode'] = df['YearsCode'].astype("float64")
df['Age1stCode'] = df['Age1stCode'].astype('float64')

# Check types of objects in dfdataframe.
type_obj = df.dtypes
print(type_obj)

# checking the correlation using the Pearson method
# ( It has a value between +1 and −1. A value of +1 is total positive linear correlation,
# 0 is no linear correlation, and −1 is total negative linear correlation.)
print(df.corr(method='pearson'))

fig, ((ax1, ax2, ax3, ax4, ax5), (ax6, ax7, ax8, ax9, ax10)) = plt.subplots(2, 5)

ax1.scatter(df['WorkWeekHrs'], df['CompTotal'])
ax1.set_title('WorkWeekHrs - CompTotal')
ax2.scatter(df['WorkWeekHrs'], df['YearsCode'])
ax2.set_title('WorkWeekHrs - YearsCode')
ax3.scatter(df['WorkWeekHrs'], df['Age'])
ax3.set_title('WorkWeekHrs - Age')
ax4.scatter(df['WorkWeekHrs'], df['Age1stCode'])
ax4.set_title('WorkWeekHrs - Age1stCode')
ax5.scatter(df['CompTotal'], df['YearsCode'])
ax5.set_title('CompTotal - YearsCode')
ax6.scatter(df['CompTotal'], df['Age'])
ax6.set_title('CompTotal - Age')
ax7.scatter(df['CompTotal'], df['Age1stCode'])
ax7.set_title('CompTotal - Age1stCode')
ax8.scatter(df['YearsCode'], df['Age'])
ax8.set_title('YearsCode - Age')
ax9.scatter(df['YearsCode'], df['Age1stCode'])
ax9.set_title('YearsCode - Age1stCode')
ax10.scatter(df['Age'], df['Age1stCode'])
ax10.set_title('Age - Age1stCode')

plt.show()

# dependent variable: YearsCode
# independent variables: Age1stCode and Age
