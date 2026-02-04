import numpy as np 

# --- 1. O Básico: Vetores 1D (dot e inner são iguais) ---
print("--- Caso 1D (Vetores) ---")
vetor_a = np.array([1, 2])
vetor_b = np.array([3, 4])
print(f"Inner: {np.inner(vetor_a, vetor_b)}") # 1*3 + 2*4 = 11
print(f"Dot:   {np.dot(vetor_a, vetor_b)}")   # 1*3 + 2*4 = 11

# --- 2. O Poder do DOT: Matrizes (Linha x Coluna) ---
# Cenário: 2 Clientes comprando 3 produtos (Arroz, Feijão, Carne)
compras = np.array([
    [2, 5, 1],  # Cliente A: 2 Arroz, 5 Feijão, 1 Carne
    [1, 0, 2]   # Cliente B: 1 Arroz, 0 Feijão, 2 Carnes
])

# Tabela de Preços em 2 Lojas (Loja X e Loja Y)
# Linhas são produtos, Colunas são as lojas
precos = np.array([
    [20, 18], # Arroz (Loja X=20, Loja Y=18)
    [10, 12], # Feijão
    [50, 45]  # Carne
])

# O dot cruza: Linhas de 'compras' com Colunas de 'precos'
custos = np.dot(compras, precos)

print("\n--- Caso 2D (Matrizes) ---")
print("Resultado (Linhas=Clientes, Colunas=Lojas):")
print(custos)
# O elemento [0,0] será o custo do Cliente A na Loja X
# O elemento [0,1] será o custo do Cliente A na Loja Y