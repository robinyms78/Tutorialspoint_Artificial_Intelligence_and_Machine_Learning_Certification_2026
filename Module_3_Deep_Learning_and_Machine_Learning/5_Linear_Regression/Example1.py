# Linear regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


# loading the data set
df = pd.read_csv("5_Linear_Regression/housing.csv")

# select lstat column as the feature X and med v column as feature y
X = df[['LSTAT']]
y = df['MEDV']

# plot data
plt.scatter(X, y)
plt.xlabel("LSTAT")
plt.ylabel("MEDV")
plt.title("LSTST vs MEDV")
plt.show()

# split data into train test splits
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# make predictions
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(mse)