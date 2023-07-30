import numpy as np

a = [1, 7, 9, 0, 3, 7, 6, 23, 678]
print("Array: ", a)
print("Minimum Value: ", np.min(a))
print("Maximum Value: ", np.max(a))
print("--------------------------------------------------------------------")

arr3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print("Matrix:")
print(arr3)
print("Maximum along axis 1:", arr3.max(axis=1))
print("Standard Deviation along axis 1:", arr3.std(axis=1))

# Count function
print("Count of elements in the array 'a':", len(a))
print("Count of elements in the matrix 'arr3':", arr3.size)