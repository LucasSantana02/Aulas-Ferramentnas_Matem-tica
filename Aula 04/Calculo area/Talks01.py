from sympy import*
import matplotlib.pyplot as plt
import numpy as np

# 1. Define a variável simbólica 'x'
x = symbols('x')

# 2. Define a função f(x) a ser integrada
f = 2**x

# 3. Calcula a integral definida de f(x) de x=0 até x=2
integral = integrate(f, (x, 0, 2))

# 4. Exibe o resultado de forma formatada
print("A área sob a curva de f(x) = 2**x de x=0 a x=2 é:")
pprint(integral)

# 5. Define os pontos para plotar a função
x_range = np.linspace(0, 2, 1000)
f = 2**x_range
plt.plot(x_range, f, label='f(x) = 2^x', color='blue') 
plt.axhline(0, color='blue', linewidth=3) # Desenha o eixo x para referência

# A condição 'where' pode ser simplificada usando a sintaxe do NumPy
plt.fill_between(x_range, f, where=(x_range > 0) & (x_range < 2), color='green', alpha=1)

plt.title('Área sob a curva de f(x) = 2^x de x=0 a x=2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()