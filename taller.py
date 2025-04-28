import matplotlib.pyplot as plt
import numpy as np

vector = np.random.rand(720).reshape(120,6).T
F = np.array(vector, order='F')
C = np.array(vector, order='C')

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.4])
ax2 = fig.add_axes([0.1, 0.5, 0.8, 0.4])

#Plot
ax1.plot(vector[1])

plt.show()

