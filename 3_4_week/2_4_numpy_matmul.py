import numpy as np

matrixA = np.array([[1,2,3], [4,5,6], [7,8,9]])
matrixB = np.array([[3,2,1], [6,5,4], [9,8,7]])

print("A * B")
print(matrixA * matrixB)
print('--------')
print("A dot B")
print(np.dot(matrixA, matrixB))
print('--------')
print("A matmul B")
print(np.matmul(matrixA, matrixB))
print('--------')
print("A @ B")
print(matrixA @ matrixB)

