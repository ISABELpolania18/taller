import matplotlib.pyplot as plt
import numpy as np

vector = np.random.rand(720).reshape(120,6).T
F = np.array(vector, order='F')
C = np.array(vector, order='C')

fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_axes([0.05, 0.55, 0.25, 0.25])
ax2 = fig.add_axes([0.35, 0.55, 0.25, 0.25])
ax3 = fig.add_axes([0.65, 0.55, 0.25, 0.25])
ax4 = fig.add_axes([0.05, 0.1, 0.25, 0.25])
ax5 = fig.add_axes([0.35, 0.1, 0.25, 0.25])

#Plot
ax1.plot(vector[0], color ='r')

#Scatter
x = np.arange(120)
ax2.scatter(x,vector[1])

#Bar
dy = 0.1
ax3.errorbar(x, vector[2], yerr=dy, fmt = '.k', ecolor='pink')

#Histograma
ax4.hist(vector[3], bins=30, alpha=0.5, color='orange', edgecolor='black')

#Pie
labels = 'Valor 1', 'Valor 2', 'Valor 3', 'Valor 4'
colors = 'orange', 'red', 'pink', 'green'
ax5.pie(vector[4][0:4], labels = labels, colors = colors, autopct='%1.1f%%')

plt.show()

