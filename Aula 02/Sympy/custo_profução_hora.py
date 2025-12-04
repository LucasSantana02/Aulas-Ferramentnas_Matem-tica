from sympy import *
x, h, c = symbols("x h c")
c = x**2 + 2*x +300
t = 20*h
hora = float(input("Digite a quantidade de horas trabalhadas: "))
hora = t.subs(h, hora)
custo = c.subs(x, hora)
print("O custo de produção para {:.0f} horas trabalhadas  é de R$ {:.2f}" . format(hora, custo))