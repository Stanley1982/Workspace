import numpy as np
import matplotlib.pyplot as plt
import math

n = 1000

thetha = np.linspace(0, 2*np.pi, 7)

x = np.cos(thetha)
y = np.sin(thetha)


x = np.random.rand(n, 1)*2 -1
y = np.random.rand(n, 1)*2 -1

for i in range(n):
    if (np.abs(x[i] <= 1)) & (np.abs(x[i])+np.abs(y[i])/np.sqrt(3) <= 1):
        plt.scatter(x[i], y[i], alpha = 0.5,linewidths= 0 )

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.show()
