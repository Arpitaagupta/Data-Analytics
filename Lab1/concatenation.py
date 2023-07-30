import numpy as np
arr = np.array([[10,20],[20,30]])
arr0 = np.zeros((2,3), dtype = arr.dtype)
print("arr : ", arr)
print("Zero Array")
print("arr0 : ", arr0)
print("---------------------------------------------------------")
print("String Concatenation of arr and arr0 : ")
print(np.concatenate((arr,arr0), axis=1))