import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np
 
# 1. Geração dos dados para a malha (grid)
x_vals = np.linspace(-5, 5, 100) 
y_vals = np.linspace(-5, 5, 100) 
X, Y = np.meshgrid(x_vals, y_vals) 
 
# Cálculo da altura (Z) para cada ponto (X, Y) da malha
Z = X**2 - Y**2 
 
# 2. Criação da figura e do ambiente 3D
fig = plt.figure(figsize=(10, 8)) # Cria uma figura com tamanho personalizado
ax = plt.axes(projection='3d') # Cria um ambiente 3D com as marcações dos eixos
 
# 3. Plotagem da superfície 3D
surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none') 
 
# 4. Customização do gráfico (rótulos, título e barra de cores)
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z (f(x,y))')
ax.set_title('Gráfico de Superfície 3D de f(x,y) = x² + y²')
fig.colorbar(surface, shrink=0.5, aspect=5) 
 
# 5. Exibição do gráfico
plt.show()