# NumPy Array Basics
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)
print(type(arr))



# Reshape
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

reshaped = arr.reshape(2, 3)

print(reshaped)



# Slicing
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])



# 2D Array Slicing
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

print(arr[0, 1])
print(arr[:, 1:])