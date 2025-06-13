import numpy as np

x = np.array([1,2,3,4,5])
y = 2 * x + 3

print(y)

a = np.array([[6, 8], [7, 9]])
b = np.array([3, 8])

ans = np.linalg.solve(a,b)
print(ans)
print(ans[0] * 6 + 8 * ans[1])
print(ans[0] * 7 + 9*ans[1])
