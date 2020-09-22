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

# Check the correlation using the Pearson method
print(df.corr(method='pearson'))

# Remove outliers, calculate the quantiles
q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
iqr = q3-q1
low_boundary = (q1 - 1.5 * iqr)
upp_boundary = (q3 + 1.5 * iqr)
df = df[~((df < low_boundary) | (df > upp_boundary)).any(axis=1)]

print(df.corr(method='pearson'))