# Random Forest Classifier
# importing the modules
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import pandas as pd

# load data set
iris = load_iris()
X = iris.data # features
y = iris.target # labels

# create pandas data frame to visualize the data
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y
df['species'] = df['target'].map(dict(zip(range(3), iris.target_names)))
print(df)

# create a random forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Take user input of columns
sepal_length = float(input('enter the sepal length(cm):'))
sepal_width = float(input('enter the sepal width(cm):'))
petal_length = float(input('enter the petal length(cm):'))
petal_width = float(input('enter the petal width(cm):'))

# create feature array of user input
user_input=[[sepal_length, sepal_width, petal_length, petal_width]]

# make predictions for the user
predictions=clf.predict(user_input)

# map the predictions to the species column
species = iris.target_names[predictions[0]]

print("predicted species:", species)
print(df['species'].unique())