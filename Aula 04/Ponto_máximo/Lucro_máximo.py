from sympy import * # Importa todas as funções da biblioteca sympy

x, y = symbols('x y') # Define as variáveis simbólicas x e y
y = -4*x**2 + 4000*x - 200000 # Define a função lucro y em termos de x

dy = diff(y, x) # Deriva a função lucro em relação a x
d2y = diff(dy, x, 2) # Deriva novamente para obter a segunda derivada

solucao = solve(Eq(dy, 0)) # Resolve a equação dy = 0 para encontrar pontos críticos
i = y.subs(x, solucao[0]) # Calcula o valor do lucro no ponto crítico encontrado
ds = d2y.subs(x, solucao[0]) # Avalia a segunda derivada no ponto crítico
print('O lucro máximo é de R$ {:.2f}, quando são produzidas e vendidas {} unidades.'.format(i, solucao[0]))