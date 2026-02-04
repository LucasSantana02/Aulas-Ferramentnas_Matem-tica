import sympy as sp
import numpy as np
# Criação de um vetor linha

u = np.array([
    [7, 1, -9]
    ])

v = np.array([
    [3, -5, -4]
    ])
# Produto Interno entre vetores linha
prod_interno = np.inner(u, v)
sp.pprint(sp.Matrix(prod_interno))