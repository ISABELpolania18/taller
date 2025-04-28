import matplotlib.pyplot as plt
import numpy as np

vector = np.random.rand(720).reshape(120,6).T
F = np.array(vector, order='F')
C = np.array(vector, order='C')

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_axes([0.1, 0.55, 0.35, 0.35])
ax2 = fig.add_axes([0.55, 0.55, 0.35, 0.35])

#Plot
ax1.plot(vector[0])

#Scatter
x = np.arange(120)
ax2.scatter(x,vector[1])

plt.show()

