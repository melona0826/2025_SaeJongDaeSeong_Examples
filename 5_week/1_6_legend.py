import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = x ** 2

plt.plot(x , y, label='Orbit')
plt.xlabel('X-Value')
plt.ylabel('Y-Value')
plt.legend()
plt.show()



