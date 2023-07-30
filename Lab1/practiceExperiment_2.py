import numpy as np

arr1 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

# a) Find sum of all elements
sum_of_all_elements = arr1.sum()
print("Sum of all elements:", sum_of_all_elements)

# b) Find sum of all elements row wise
sum_row_wise = arr1.sum(axis=2)
print("Sum of all elements row-wise:")
print(sum_row_wise)

# c) Find sum of all elements column wise
sum_column_wise = arr1.sum(axis=0)
print("Sum of all elements column-wise:")
print(sum_column_wise)

# d) Find max of all elements
max_element = arr1.max()
print("Max of all elements:", max_element)

# e) Find min of all elements in each row
min_row_wise = arr1.min(axis=2)
print("Min of all elements in each row:")
print(min_row_wise)

# f) Find mean of all elements in each row
mean_row_wise = arr1.mean(axis=2)
print("Mean of all elements in each row:")
print(mean_row_wise)

# g) Find column-wise standard deviation
std_column_wise = arr1.std(axis=0)
print("Column-wise standard deviation:")
print(std_column_wise)

