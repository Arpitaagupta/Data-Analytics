import numpy as np

# Load the dataset from the 'student.txt' file, excluding the first column (roll numbers)
scores = np.loadtxt('student.txt', dtype='int', delimiter=',', usecols=range(1, 6))

# a) Find sum of all elements
total_sum = np.sum(scores)

# b) Find sum of all elements row wise
row_sum = np.sum(scores, axis=1)

# c) Find sum of all elements column wise
column_sum = np.sum(scores, axis=0)

# d) Find max of all elements
max_value = np.max(scores)

# e) Find min of all elements in each row
row_min = np.min(scores, axis=1)

# f) Find mean of all elements in each row
row_mean = np.mean(scores, axis=1)

# g) Find column-wise standard deviation
column_std = np.std(scores, axis=0)

#considering roll no at 0th index of every row

# Print the results
print("a) Sum of all elements:", total_sum)
print("b) Sum of all elements row-wise:", row_sum)
print("c) Sum of all elements column-wise:", column_sum)
print("d) Max of all elements:", max_value)
print("e) Min of all elements in each row:", row_min)
print("f) Mean of all elements in each row:", row_mean)
print("g) Column-wise standard deviation:", column_std)