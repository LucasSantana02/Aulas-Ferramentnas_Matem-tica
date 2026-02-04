from sympy import * # Importa todas as funções da biblioteca sympy
x, f = symbols('x f') # Define as variáveis simbólicas x e f
f = -2*x**3 - 4*x**2 +13*x - 1 # Define a função f
df = diff(f, x, 2) # Calcula a derivada de f em relação a x
pprint(df) # Imprime a derivada de forma legível