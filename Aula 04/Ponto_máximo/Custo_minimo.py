from sympy import *
import matplotlib.pyplot as plt
import numpy as np

x, y = symbols('x y') # Define as variáveis simbólicas x e y
y = x**2 - 20*x +3000 # Define a função custo y em termos de x
dy = diff(y, x) # Deriva a função custo em relação a x
d2y = diff(dy, x, 2) # Deriva novamente para obter a segunda derivada
solution = solve(Eq(dy, 0)) # Resolve a equação dy = 0 para encontrar pontos críticos
ponto = y.subs(x, solution[0]) # Calcula o valor do custo do ponto crítico encontrado
print('O custo mínimo é de R$ {:.2f} e ocorre quando são produzidas {} unidades.'.format(ponto, solution[0]))


# Plotando a função custo
x = np.linspace(0, 30, 100)
y = x**2 - 20*x +3000
plt.plot(x, y, label='Custo')

plt.xlabel('Unidades Produzidas')
plt.ylabel('Custo')
plt.title('Custo Mínimo')
plt.legend()
plt.grid(True)
plt.show()