import numpy as np

matrixA = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("A")
print(matrixA)
print("-------")


print("np.sum(matrixA, axis = 0)")
print(np.sum(matrixA, axis=0))
print("-------")


print("np.sum(matrixA, axis = 1)")
print(np.sum(matrixA, axis=1))
print("-------")


print("np.mean(matrixA, axis = 0)")
print(np.mean(matrixA, axis=0))
print("-------")

print("np.mean(matrixA, axis = 1)")
print(np.mean(matrixA, axis=1))
print("-------")


print("np.min(matrixA, axis = 0)")
print(np.min(matrixA, axis=0))
print("-------")

print("np.min(matrixA, axis = 1)")
print(np.min(matrixA, axis=1))
print("-------")


print("np.max(matrixA, axis = 0)")
print(np.max(matrixA, axis=0))
print("-------")

print("np.max(matrixA, axis = 1)")
print(np.max(matrixA, axis=1))
print("-------")


print("np.zeros((2,3))")
print(np.zeros((2,3)))
print("-------")


print("np.ones((2,3))")
print(np.ones((2,3)))
print("-------")


print("np.arange(1,10,2)")
print(np.arange(1,10,2))
print("-------")


print("np.linspace(0,1,5)")
print(np.linspace(0,1,5))
print("-------")


print("np.random.random((3,2))")
print(np.random.random((3,2)))
print("-------")


print("np.random.randn(3,2)")
print(np.random.randn(3,2))
print("-------")
