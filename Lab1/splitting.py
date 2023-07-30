import numpy as np
arr2 = np.array([[1,2],[3,4]])
print("arr2 : ", arr2)
print("Splitting")
print("Axis = 0")
print(np.split(arr2, 2, axis=0))
print("---------------------------------------------------------------------")
print("Axis = 1")
print(np.split(arr2, 2, axis=1))