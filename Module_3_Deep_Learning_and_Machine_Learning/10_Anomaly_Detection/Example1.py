# importing libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.datasets import load_breast_cancer

breast_cancer = load_breast_cancer()
X = breast_cancer.data

# perform anomaly detection with isolation forest
clf = IsolationForest(contamination=0.1, random_state=42)
clf.fit(X)

y_pred = clf.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.title('anomaly detection using isolation forest')
plt.show()