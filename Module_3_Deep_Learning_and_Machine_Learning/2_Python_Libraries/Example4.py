# Matplotlib

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

# load diabetes data
diabetes=load_diabetes()

x = diabetes.data
y = diabetes.target

# line plot
plt.figure()
plt.plot(y)
plt.title('diabetes progression')
plt.xlabel('samples')
plt.ylabel('target')
plt.show()

# scatter plot
plt.figure()
plt.scatter(x[:, 2], y)
plt.title('diabetes progression')
plt.xlabel('body mass index')
plt.ylabel('target')
plt.show()

# bar plot
target=np.bincount(y.astype(int))
plt.figure()
plt.bar(np.arange(len(target)), target)
plt.title('diabetes progression')
plt.xlabel('target distribution')
plt.ylabel('target')
plt.show()

# histogram
plt.figure()
plt.hist(x[:,0], bins=30, alpha=0.7)
plt.title('diabetes progression')
plt.xlabel('age')
plt.ylabel('frequency')
plt.show()

# https://matplotlib.org/stable/plot_types/index.html