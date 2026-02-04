import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

l, x = sp.symbols('l x')  # Define as variáveis simbólicas l e x
l = -120*x**2 + 4800*x # Define a função lucro l em termos de x
dl = sp.diff(l, x)  # Deriva a função lucro em relação a x

# Resolve a equação dl = 0 para encontrar os pontos críticos e armazena o resultado
# A função solve retorna uma lista, então pegamos o primeiro (e único) elemento com [0]
ponto_critico = sp.solve(dl, x)

# Calcula o lucro máximo substituindo o valor de x encontrado na função de lucro original
lucro_max = l.subs(x, ponto_critico[0])

# Plotando a função lucro
x_vals = np.linspace(0, 50, 400)
l_vals = -120*x_vals**2 + 4800*x_vals
plt.plot(x_vals, l_vals, label='Função Lucro', color='blue')
plt.xlabel('Unidades Produzidas e Vendidas')
plt.ylabel('Lucro (R$)')
plt.title('Lucro Máximo')

# Adiciona um marcador no ponto de lucro máximo
ponto_critico_val = ponto_critico[0]
plt.scatter(ponto_critico_val, lucro_max, color='red', zorder=5, label=f'Lucro Máximo (x={ponto_critico_val})')
plt.axvline(x=ponto_critico_val, color='gray', linestyle='--', linewidth=1) # Linha vertical de referência

plt.legend()
plt.grid(True)
plt.show()

print(f"O lucro máximo é de: {lucro_max}.")
print(f'Para o lucro máximo ser alcançado, devem ser produzidas e vendidas {ponto_critico_val} unidades.')