import numpy as np
import sympy as sp

a = np.array([[3,4],[1,1]])
b = np.array([[1900], [550]])
x = sp.Matrix(np.linalg.solve(a,b))
sp.pprint(x)