from sympy import *
x, f = symbols('x f')
f = 20*x + 100
metro = float(input("Digite a metragem quadrada da casa: "))
custo = f.subs(x, metro)
print(f"O custo da serviço do porcelanato é de: R$ {custo:.2f}")