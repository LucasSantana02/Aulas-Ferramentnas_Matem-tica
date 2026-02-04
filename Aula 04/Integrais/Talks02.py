from sympy import*

f, x = symbols('f x')
f = 2*x +ln(x)
derivada = diff(f, x)
integral = integrate(derivada, x)
pprint('A derivada da função é: %s ' %derivada)
pprint('A integral da função é: %s ' %integral)