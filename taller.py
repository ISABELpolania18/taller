import matplotlib.pyplot as plt
import numpy as np

vector = np.random.rand(720).reshape(120,6).T
F = np.array(vector, order='F')
C = np.array(vector, order='C')

fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_axes([0.05, 0.55, 0.25, 0.25])
ax2 = fig.add_axes([0.38, 0.55, 0.25, 0.25])
ax3 = fig.add_axes([0.7, 0.55, 0.25, 0.25])
ax4 = fig.add_axes([0.05, 0.1, 0.25, 0.25])
ax5 = fig.add_axes([0.38, 0.1, 0.25, 0.25])
ax6 = fig.add_axes([0.7, 0.1, 0.25, 0.25])

#Plot
ax1.plot(vector[0], color ='r')
ax1.grid(True)
ax1.set_title('Plot')
ax1.set_xlabel('eje x')
ax1.set_ylabel('eje y')

#Scatter
x = np.arange(120)
ax2.scatter(x,vector[1])
ax2.set_title('Scatter')
ax2.set_xlabel('eje x')
ax2.set_ylabel('eje y')


#Bar
dy = 0.1
ax3.errorbar(x, vector[2], yerr=dy, fmt = '.k', ecolor='pink')
ax3.grid(True)
ax3.set_title('ErrorBar')
ax3.set_xlabel('eje x')
ax3.set_ylabel('eje y')

#Histograma
ax4.hist(vector[3], bins=30, alpha=0.5, color='orange', edgecolor='black')
ax4.set_title('Histograma')
ax4.set_xlabel('Valor')
ax4.set_ylabel('Frecuencia')

#Pie
labels = 'Valor 1', 'Valor 2', 'Valor 3', 'Valor 4'
colors = 'orange', 'red', 'pink', 'green'
ax5.pie(vector[4][0:4], labels = labels, colors = colors, autopct='%1.1f%%')
ax5.set_title('Pie')

#Plot 2
m = vector[5]
y= 2 * m**2 - 3 * m + 1 
ax6.plot(y, color = 'purple')
ax6.grid(True)
ax6.set_title('Otro Plot')
ax6.set_xlabel('eje x')
ax6.set_ylabel('eje y')

plt.show()

