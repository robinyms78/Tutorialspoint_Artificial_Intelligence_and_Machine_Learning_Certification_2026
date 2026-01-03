# Numpy

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)

# sum of elements
print(np.sum(arr))

# mean of elements
print(np.mean(arr))

# reshaping of array
arr2 = np.reshape(arr, (3, 3))
print(arr2)

# broadcasting function
arr3 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(arr3)

arr_broad = arr + arr3
print(arr_broad)

# vectorized multiplication
print(np.multiply(arr, arr_broad))

# random number generating function
random_arr = np.random.rand(7)
print('random_array', random_arr)

# element wise comparison
arr4 = np.array([1, 3, 4, 7, 9])
arr5 = np.array([2, 3, 5, 6, 9])
print(np.equal(arr4, arr5))

# sorting of array
arr6 = np.array([1, 5, 4, 7, 9])
print(np.sort(arr6))

# https://numpy.org/doc/stable/user/index.html#user