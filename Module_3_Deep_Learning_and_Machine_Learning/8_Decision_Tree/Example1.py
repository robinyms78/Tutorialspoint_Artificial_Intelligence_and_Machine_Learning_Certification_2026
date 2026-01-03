# XGBoost

# import libraries
import numpy as np
import pandas as pd
import xgboost as xgb

# load the data set
dataset = pd.read_csv("8_Decision_Tree/diabetes.csv")
print(dataset)

# prepare the data
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,-1].values

# create and train the xgboost model
xgb_model = xgb.XGBClassifier()
xgb_model.fit(X, y)

# take user input for the feature values
user_input=[]

# taking user input for each feature available
for feature in dataset.columns[:-1]:
    value = float(input("enter the value for {}:".format(feature)))
    user_input.append(value)

# make predictions
user_input=np.array(user_input).reshape(1, -1)
prediction=xgb_model.predict(user_input)

if prediction[0] == 0:
    print("The model predicts that diabetes is not diagnosed")
else:
    print("The model predicts that diabetes is diagnosed")

# https://www.geeksforgeeks.org/machine-learning/xgboost/