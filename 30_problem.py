import numpy as np

# Create matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Addition
print("Addition:\n", matrix1 + matrix2)

# Subtraction
print("\nSubtraction:\n", matrix1 - matrix2)

# Multiplication
print("\nMultiplication:\n", np.dot(matrix1, matrix2))

# Inverse of matrix1
print("\nInverse of Matrix1:\n", np.linalg.inv(matrix1))

# Inverse of matrix2
print("\nInverse of Matrix2:\n", np.linalg.inv(matrix2))
