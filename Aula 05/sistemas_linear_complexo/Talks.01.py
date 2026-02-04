import numpy as np
import sympy as sp

a = np.array([[complex(2, 3), complex(0, 5)],
              [complex(5, 0), complex(3, 3)]])
b = np.array([[complex(3, 7)],
              [complex(6, -7)]])
x = sp.Matrix(np.linalg.solve(a, b))
sp.pprint(x)