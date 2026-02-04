import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x, f = sp.symbols('x f')

# Definindo a função de consumo
f=-0.04185*x**4+2.52027*x**3-54.81718*x**2+509.27586*x-1624.86959
# Derivando a função
df = sp.diff(f, x)
# Encontrando os pontos críticos
pontos_criticos = sp.solve(sp.Eq(df, 0), x)

# Para classificar os pontos, usamos a segunda derivada
d2f = sp.diff(df, x)
print(pontos_criticos)
print(f'Mínimo: {pontos_criticos[0]}')
print(f'Máximo: {pontos_criticos[1]}')

#Plotando a função e os pontos críticos
x = np.linspace(12, 22, 100)
f = -0.04185*x**4 + 2.52027*x**3 - 54.81718*x**2 + 509.27586*x - 1624.86959
plt.plot(x, f, label= 'Função de Consumo')
plt.xlabel('Horario do Dia')
plt.ylabel('Consumo de lanches')
plt.title('Consumo Máximo e Mínimo de Lanches ao Longo do Dia')
plt.axvline(pontos_criticos[0], color='red', linestyle='--', label='Mínimo')
plt.axvline(pontos_criticos[1], color='green', linestyle='--', label='Máximo')
plt.legend()
plt.grid(True)
plt.show()