import matplotlib.pyplot as plt
import numpy as np

# Define a lista de valores para x usando linspace
x = np.linspace(0, 200, 100)  # Gera 100 valores de 0 a 200
r = 419*x # Calcula os valores de r para cada x usando a equação r = 419*x
c = 271*x + 15000 # Calcula os valores de c para cada x usando a equação c = 271*x + 15000
plt.plot(x, r, label='Receita de vendas') # Plota o gráfico de receita r
plt.plot(x, c, label='Custos de produção') # Plota o gráfico de custos c
plt.title('Gráfico de Receita e Custos') # Adiciona um título ao gráfico
plt.xlabel('Quantidade de unidades vendidas') # Adiciona o rótulo do eixo x
plt.ylabel('Valor em Reais (R$)') # Adiciona o rótulo do eixo y
plt.legend() # Adiciona a legenda ao gráfico
plt.grid(True) # Adiciona uma grade ao gráfico
plt.show() # Exibe o gráfico