from sympy import* # Importa todas as funções da biblioteca sympy
h, x = symbols('h x') # Define as variáveis simbolicas h e x
h = sin(x) # Define a função h em relação a x
dh = diff(h,x) # Clacula a derivada de h em relação a x
pprint(dh) # Improme a derivada de forma legível