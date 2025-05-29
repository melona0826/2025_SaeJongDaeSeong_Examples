import numpy as np

# 1) 직접 미분식을 구하고 최댓값 계산
x = np.linspace(1,6,100)
y = 2 * x

print("Method 1")
print(np.max(y))
print("----------")


# 2) 도함수를 이용하여 계산
def derivative(f, x, h=0.000001) :
  return (f(x + h) - f(x)) / h

def f(x) :
  return x ** 2 + 3

print("Method 2")
print(np.max(derivative(f, x)))

