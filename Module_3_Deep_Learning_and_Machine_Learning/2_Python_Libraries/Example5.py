# Seaborn

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
import pandas as pd

# load diabetes data set
diabetes = load_diabetes()
x = diabetes.data
y = diabetes.target
a = pd.read_csv("2_Python_Libraries/diabetes.csv")
print(a)

# scatter plot
sns.regplot(x=x[:, 2], y=y)
plt.title("bmi vs diabetes progression")
plt.xlabel('bmi')
plt.ylabel('diabetes progression')
plt.show()

# box plot
sns.boxplot(x='Pregnancies', y='Age', data=a)
plt.title("age distribution by sex")
plt.xlabel('sex')
plt.ylabel('age')
plt.show()

# heat map
corr_matrix = a.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("correlation matrix")
plt.show()

# https://seaborn.pydata.org/