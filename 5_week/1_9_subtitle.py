import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y1 = x ** 2

y2 = x ** 3

plt.subplot(2,1,1)
plt.plot(x , y1)
plt.xlabel('X-Value')
plt.ylabel('Y-Value')
plt.title('Orbit Graph 1')

plt.subplot(2,1,2)
plt.plot(x , y2)
plt.xlabel('X-Value')
plt.ylabel('Y-Value')
plt.title('Orbit Graph 2')
plt.show()








