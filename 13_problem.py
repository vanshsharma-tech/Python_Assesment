# NumPy program to create a 5x5 matrix
# and perform matrix operations

import numpy as np

# Create a 5x5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, (5, 5))

# Display original matrix
print("Original 5x5 Matrix:\n")
print(matrix)

# Calculate row-wise sum
row_sum = np.sum(matrix, axis=1)

# Calculate column-wise sum
column_sum = np.sum(matrix, axis=0)

# Calculate transpose of matrix
transpose_matrix = matrix.T

# Calculate determinant
determinant = np.linalg.det(matrix)

# Display row-wise sum
print("\nRow-wise Sum:\n")
print(row_sum)

# Display column-wise sum
print("\nColumn-wise Sum:\n")
print(column_sum)

# Display transpose matrix
print("\nTranspose of Matrix:\n")
print(transpose_matrix)

# Display determinant
print("\nDeterminant of Matrix:\n")
print(determinant)
