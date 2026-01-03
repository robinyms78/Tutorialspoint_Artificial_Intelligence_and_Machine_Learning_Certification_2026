# Scipy

import numpy as np
from numpy import sqrt, sin, cos, tan, exp
from scipy import integrate, interpolate, optimize, linalg, signal, stats, sparse

a = sqrt(9)
print(a)

angle=45
print(sin(angle))
print(cos(angle))
print(tan(angle))

# numerical integration
result, error = integrate.quad(lambda x: np.sin(x), 0, np.pi)
print(result)

# optimization
def objective(x):
    return (x - 2)**2 + 1

b = optimize.minimize(objective, x0=0)
print(b.x)

# linear algebra
a = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
x = linalg.solve(a, b)
print(x)

# signal processing
t = np.linspace(0, 1, 500)
x = np.sin(2*np.pi*5*t) + np.random.rand(t.size)*0.5
filtered=signal.medfilt(x)
print(filtered)

# sparse matrices
c = sparse.csc_matrix([[1, 2, 5], [1, 2, 3], [4, 3, 5]])
b = sparse.csc_matrix([[1, 2, 0], [0, 0, 3], [4, 0, 5]])
c = c.dot(b)
print(c.toarray())

# https://docs.scipy.org/doc/scipy/tutorial/index.html