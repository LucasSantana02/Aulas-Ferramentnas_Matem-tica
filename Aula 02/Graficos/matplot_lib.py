import matplotlib.pyplot as plt
# Define a lista de valores para x
x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Calcula os valores de y para cada x usando a equação y = x²
y = [i**2 for i in x]

plt.plot(x, y)
plt.title('Grafico de y = x²')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.show()