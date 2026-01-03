import pandas as pd 
from sklearn.linear_model import LogisticRegression

# load the data set
dataset = pd.read_csv("/home/robin/Self-Learning/tutorialspoint_artificial_intelligence_and_machine_learning_ce/Module_3_Deep_Learning_and_Machine_Learning/7_Logistic_Regression/diabetes.csv")
print(dataset)

# prepare the data
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

# create and train the machine learning model
logreg = LogisticRegression()
logreg.fit(X, y)

# take user input for the feature values
user_input = []

# taking user input for each feature available
for feature in dataset.columns[:-1]:
    value = float(input("Enter the value for {}:".format(feature)))
    user_input.append(value)

# making predictions for user input
user_input=[user_input]
prediction=logreg.predict(user_input)

if prediction[0]==0:
    print("The model predicts that diabetes is not diagnosed")
else:
    print("The model predicts that diabetes is diagnosed")