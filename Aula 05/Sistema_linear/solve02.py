import numpy as np
import sympy as sp 

a = np.array([[3,4,-2],[1,-1,4],[-4,1,1]])
b = np.array([[8], [19], [0]])
x = sp.Matrix(np.linalg.solve(a, b))
sp.pprint(x)