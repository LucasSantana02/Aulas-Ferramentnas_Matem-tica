from sympy import *
x, c = symbols("x c")
c = 0.04*x**3 -4*x**2 + 101*x + 5000
unidade = float(input("Digite a quantidade de unidades produzidas: "))
custo = c.subs(x, unidade)
print(f"O custo de produção para {unidade} unidades é de R$ {custo:.2f}")