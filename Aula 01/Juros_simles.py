import sympy as sp

c = 566.00
m = 614.30
n = 6
juros = float(m-c)
taxa = juros/n/c
i = round(taxa*100,2)
print(f'A taxa de crescimento anual é de {i}%')