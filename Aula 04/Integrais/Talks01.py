from sympy import*

f, x = symbols('f x')
f = -2*x**3 - 4*x**2 +13*x - 1
derivada = diff(f, x)
integral = integrate(derivada, x)
print(f'A derivada da função é: {derivada} ')
print(f'A integral da função é: {integral} ')