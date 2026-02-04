from sympy import * # Importa todas as funções da biblioteca sympy
t, x = symbols('t x') # Define as variáveis simbolicas t e x
t = (3*x**2 - 4*x) / (2*x**3+6) # Define a função t em relação a x
dt = diff(t,x) # Clacula a derivada de t em relação a x
pprint(dt) # Imprime a derivada de forma legível