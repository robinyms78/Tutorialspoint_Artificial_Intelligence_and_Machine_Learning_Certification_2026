import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 
from sklearn import datasets

# load the data set
iris = datasets.load_iris()
X = iris.data

# perform kmean clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
y_pred = kmeans.predict(X)

# plot the results
plt.scatter(X[:,0], X[:,1], c=y_pred)
plt.show()