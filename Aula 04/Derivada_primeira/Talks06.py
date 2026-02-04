from sympy import * # Importa todas as funções da biblioteca sympy
v, x = symbols('v x') # Define as variáveis simbolicas v e x
v = (x**2 - 5*x)**0.5 # Define a função v em relação a x
dv = diff(v,x) # Clacula a derivada de v em relação a x
pprint(dv) # Imprime a derivada de forma legível