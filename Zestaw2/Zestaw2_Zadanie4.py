import pandas as pd
from sklearn import model_selection
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

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

map_values = {'Yes': 1, 'No': 0}
df['BetterLife'] = df['BetterLife'].map(map_values)
df = df[df['Gender'].isin(['Woman', 'Man'])]
df = pd.get_dummies(df, columns=['Gender'])

type_obj = df.dtypes

print(type_obj)

# Remove outliers, calculate the quantiles
q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
iqr = q3-q1
low_boundary = (q1 - 1.5 * iqr)
upp_boundary = (q3 + 1.5 * iqr)
df = df[~((df < low_boundary) | (df > upp_boundary)).any(axis=1)]

# Generate descriptive statistics.
print(df.describe())

# Dividing the data into a training set and a test set - simple division.
splits1 = model_selection.train_test_split(df[['Age']], df['YearsCode'], test_size=.33, random_state=0)
X1_train, X1_test, y1_train, y1_test = splits1
print(X1_train.shape, X1_test.shape, y1_train.shape, y1_test.shape)
splits2 = model_selection.train_test_split(df[['Age', 'Age1stCode']], df['YearsCode'], test_size=.33, random_state=0)
X2_train, X2_test, y2_train, y2_test = splits2
print(X2_train.shape, X2_test.shape, y2_train.shape, y2_test.shape)
splits3 = model_selection.train_test_split(df[['Age', 'Age1stCode', 'Gender_Man', 'Gender_Woman', 'BetterLife']], df['YearsCode'], test_size=.33, random_state=0)
X3_train, X3_test, y3_train, y3_test = splits3
print(X3_train.shape, X3_test.shape, y3_train.shape, y3_test.shape)

# Create the regression model.
regr_one = linear_model.LinearRegression()
regr_two = linear_model.LinearRegression()
regr_three = linear_model.LinearRegression()
# Fit the model.
regr_one.fit(X1_train, y1_train)
regr_two.fit(X2_train, y2_train)
regr_three.fit(X3_train, y3_train)
# Calculate coefficients.
coefficients1 = regr_one.coef_
coefficients2 = regr_two.coef_
coefficients3 = regr_three.coef_
# Calculate the mean squared error.
mse1 = mean_squared_error(y1_test, regr_one.predict(X1_test))
mse2 = mean_squared_error(y2_test, regr_two.predict(X2_test))
mse3 = mean_squared_error(y3_test, regr_three.predict(X3_test))

print('Data for the first model: 1) coefficients : '+str(coefficients1)+', 2) mean squared error: '+str(mse1))
print('Data for the second model: 1) coefficients : '+str(coefficients2)+', 2) mean squared error: '+str(mse2))
print('Data for the third model: 1) coefficients : '+str(coefficients3)+', 2) mean squared error: '+str(mse3))