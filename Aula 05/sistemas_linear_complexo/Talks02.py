import numpy as np
import sympy as sp

a = np.array([[complex(8, 4), complex(-3, -4)],
              [complex(-3, -4), complex(8, -1)]])
x1 = np.cos(np.deg2rad(0))
y1 = np.sin(np.deg2rad(0))
x2 = np.cos(np.deg2rad(-150))
y2 = np.sin(np.deg2rad(-150))
b = np.array([[100 * complex(x1,y1)],
              [50 * complex(x2, y2)]])
solução = sp.Matrix(np.linalg.solve(a, b))
sp.pprint(solução)