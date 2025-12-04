from sympy import *
x = symbols('x')
expansão = expand((x**2 + 1) * (x**2 + 3*x + 6))
pprint(expansão)