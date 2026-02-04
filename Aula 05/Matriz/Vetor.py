import sympy as sp 
import numpy as np
# Criação de um vetor linha
v = np.array([35.00, 16.40, 8.49, 15.56])
w = 4*v
sp.pprint(sp.Matrix(w))