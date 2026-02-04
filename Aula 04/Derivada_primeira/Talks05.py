from sympy import * # Importa todas as funções da biblioteca sympy
q, x = symbols('q x') # Define a variável simbólica x
q = sin(x) * cos(x) # Define a função q
dq = diff(q, x) # Calcula a derivada de q em relação a x
pprint(dq) # Imprime a derivada de forma legível