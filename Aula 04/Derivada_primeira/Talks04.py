from sympy import * # Importa todas as funções da biblioteca sympy
r, x = symbols('r x') # Define as variáveis simbolicas r e x
r = tan(x) # Define a função r em relação a x
dr = diff(r,x) # Clacula a derivada de r em relação a x
pprint(dr) # Improme a derivada de forma legível