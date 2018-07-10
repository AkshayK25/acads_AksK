import numpy as np
import math

# Question 1

print("--------------------------------------Playing with Numpy------------------------------------------------------")
x = np.random.rand(10, 1)
print(x)
print("Mean of x ->", x.mean())
print("-----------------------------------------------------------------------------------------------")

# Question 2
print("-----------------------------------------------------------------------------------------------")
y = np.random.rand(20, 1)
print(y)
print("Standard_deviation of y ->", y.std())
print("Variance of y is ->", np.var(y, ddof=1))
print("-----------------------------------------------------------------------------------------------")

# Question 4

# Create numpy array Matrix
Matrix = np.random.rand(10,1)
print("--------------------------------------------------------------------------------------------------")
print(Matrix)

# Defination of the function to be applied


def funk(x):
    return 1 / (1 + np.exp(-x))


#  Apply the function on Matrix
output = np.apply_along_axis(funk, 0, Matrix)
print(output)
print("--------------------------------------------------------------------------------------------------")

# Question 3
print("------------------------------------------------------------------------------------------------")
matrix1 = np.random.random((10, 20))
print(matrix1)
matrix2 = np.random.random((20, 25))
print(matrix2)
matrix3 = np.dot(matrix1, matrix2)
print("Dot_product of 2 matrices ->", matrix3)
print("Shape of new Matrix:", np.shape(matrix3))
print("Sum of all the elements of new matrix:", np.sum(matrix3))
print("----------------------End of the program--------------------------------------------------------")
