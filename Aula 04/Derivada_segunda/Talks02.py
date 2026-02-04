from sympy import * # Importa todas as funções da biblioteca sympy
g, x = symbols('g x') # Define as variáveis simbolicas g e x
g = 2*x+ln(x) # Define a função g
dg = diff(g,x, 2) # Clacula a derivada de g em relação a x
pprint(dg) # Improme a derivada de forma legível