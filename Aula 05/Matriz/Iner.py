import numpy as np 

# --- Exemplo Prático: Caixa de Supermercado ---
# Preços dos produtos: [Arroz, Feijão, Carne]
precos = np.array([
    [20.00, 10.00, 50.00],
    [30.00, 12.00, 45.00]
    ])

# --- CASO 1: Um único cliente (Vetor 1D) ---
# Cliente comprou: 2 arroz, 5 feijão, 1 carne
carrinho = np.array([2, 5, 1])

# Conta: (20*2) + (10*5) + (50*1) = 40 + 50 + 50 = 140
total = np.inner(precos, carrinho)
print(f"Total a pagar (1 Cliente): R$ {total}")

# --- CASO 2: Vários clientes na fila (Matriz 2D) ---
# Cada LINHA é o carrinho de um cliente diferente
fila_clientes = np.array([
    [2, 5, 1],  # Cliente A (mesmo de cima)
    [1, 0, 2]   # Cliente B (1 arroz, 0 feijão, 2 carnes)
])

# O inner calcula o total para CADA LINHA separadamente
totais = np.inner(fila_clientes, precos)
print(f"Totais a pagar (Cliente A, Cliente B): {totais}")