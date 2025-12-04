import matplotlib.pyplot as plt
import numpy as np

# Define a lista de valores para x usando linspace
x = np.linspace(-5, 5, 100)  # Gera 100 'valores de -5 a 5
y = []
for i in x:
    y.append(i**2) # Calcula os valores de y para cada x gerado na função linspace usando a equação y = x²
plt.plot(x, y, label=('Função y = x²')) # Plota o gráfico de y = x²
plt.title('Gráfico de y = x²') # Adiciona um título ao gráfico
plt.xlabel('Eixo X') # Adiciona o rótulo do eixo x
plt.ylabel('Eixo Y') # Adiciona o rótulo do eixo y
plt.legend() # Adiciona a legenda ao gráfico
plt.grid(True) # Adiciona uma grade ao gráfico
plt.show() # Exibe o gráfico