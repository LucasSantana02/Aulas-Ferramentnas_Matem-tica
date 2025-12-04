from sympy import *
x, r, c = symbols('x r c')
r = 3500*x
c = 1800*x + 27200
equilibrio = solve(Eq(r, c), x)
receita = r.subs(x, equilibrio[0])
custo = c.subs(x, equilibrio[0])
print('No ponto de equilíbrio, a receita e o custo são iguais a: R$ {:.2f}.'.format(receita))
print('Para não haver prejuízo, a quantidade mínima a ser vendida é: {}'.format(equilibrio[0]))