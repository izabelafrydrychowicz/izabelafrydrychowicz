import pandas as pd
from sklearn import model_selection
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns


# Read file and create a dataframe.
df = pd.read_csv("survey_results_public.csv", header=0,
                 usecols=['YearsCode', 'Age', 'Age1stCode'])

# Remove missing values.
df = df.dropna()

df.loc[df['YearsCode'] == 'Less than 1 year'] = 0
df.loc[df['YearsCode'] == 'More than 50 years'] = 51
df.loc[df['Age1stCode'] == 'Younger than 5 years'] = 0
df.loc[df['Age1stCode'] == 'Older than 85'] = 86
df['YearsCode'] = df['YearsCode'].astype("float64")
df['Age1stCode'] = df['Age1stCode'].astype('float64')

print(df.corr(method='pearson'))

sns.set()
plt.plot(df['Age'],df['YearsCode'],'ro', markersize=0.3)
plt.show()
plt.plot(df['Age1stCode'],df['YearsCode'],'ro', markersize=0.3)
plt.show()

# Remove outliers, calculate the quantiles
q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
iqr = q3-q1
low_boundary = (q1 - 1.5 * iqr)
upp_boundary = (q3 + 1.5 * iqr)
df = df[~((df < low_boundary) | (df > upp_boundary)).any(axis=1)]

print(df.corr(method='pearson'))

sns.set()
plt.plot(df['Age'],df['YearsCode'],'ro', markersize=0.3)
plt.show()
plt.plot(df['Age1stCode'],df['YearsCode'],'ro', markersize=0.3)
plt.show()

# Generate descriptive statistics.
print(df.describe())

# Dividing the data into a training set and a test set - simple division.
splits2 = model_selection.train_test_split(df[['Age', 'Age1stCode']], df['YearsCode'], test_size=.33, random_state=0)
X2_train, X2_test, y2_train, y2_test = splits2
print(X2_train.shape, X2_test.shape, y2_train.shape, y2_test.shape)

regr_two = linear_model.LinearRegression()
regr_two.fit(X2_train, y2_train)
coefficients2 = regr_two.coef_
mse2 = mean_squared_error(y2_test, regr_two.predict(X2_test))
print('Data for the selected model: 1) coefficients : '+str(coefficients2)+', 2) mean squared error: '+str(mse2))

