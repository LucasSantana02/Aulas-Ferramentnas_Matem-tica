import numpy as np
import sympy as sp
a = np.array([[1,1],[2,1]])
b = np.array([[22],[34]])
x = sp.Matrix(np.linalg.solve(a,b))
sp.pprint(x)