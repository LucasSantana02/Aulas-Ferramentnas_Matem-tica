import matplotlib.pyplot as plt #Impora a biblioteca matplotlib
import numpy as np #Importa a biblioteca numpy para a função linspace

# Define a lista de valores para x usando linspace
x = np.linspace(-0, 30, 100) # Gera 100 valores de zero a trinta
r = 3500*x # Calcula os valores de r para cada x usnando a equação r = 3500*x
c = 1800*x + 27200 # Calcula oss valores de c para cada x usando a equação c = 1800*x + 27200
plt.plot(x, r, label='Receita r = 3500*x') # Plota o gráfico da receita
plt.plot(x, c, label='Custo c = 1800*x + 27200') # Plota o gráfico do custo
plt.title('Gráfico de Receita e Custo') # Adiciona o título ao gráfico
plt.xlabel('Eixo X') # Adiciona o rótulo do eixo x
plt.ylabel('Eixo Y') # Adiciona o rótulo do eixo y
plt.legend() # Adiciona a legenda ao gráfico
plt.show() # Exibe o gráfico