import matplotlib.pyplot as plt
import numpy as np

vector = np.random.rand(720).reshape(120,6).T
F = np.array(vector, order='F')
C = np.array(vector, order='C')
