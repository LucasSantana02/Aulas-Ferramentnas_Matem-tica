import sympy as sp
x,y = sp.symbols('x y')
f = sp.factor(x**2*y**5+3*x**3*y**4-x**3*y**6)
sp.pprint(f)