from sympy import symbols, factor, pprint
x, y = symbols("x y")
fatoração = factor(2*x**4 + 8*x**3 + 10*x**2)
pprint(fatoração)

fatoração1 = factor(x*y**3 + 2*x**2*y**4)
pprint(fatoração1)