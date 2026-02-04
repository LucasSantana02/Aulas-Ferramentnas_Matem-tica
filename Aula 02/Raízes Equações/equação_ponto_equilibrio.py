from sympy import symbols, Eq, solve
x, r, c = symbols('x r c')
r = 3500*x
c = 1800*x + 27200
solucao = solve(Eq(r, c), x)

# Verifica se a solução foi encontrada e extrai o valor
if solucao:
    ponto_equilibrio_x = solucao[0]
    receita = r.subs(x, ponto_equilibrio_x)
    # O custo será igual à receita no ponto de equilíbrio, então não é necessário recalcular.
    
    print('No ponto de equilíbrio, a receita e o custo são iguais a: R$ {:.2f}.'.format(receita))
    print('Para não haver prejuízo, a quantidade mínima a ser vendida é: {}'.format(ponto_equilibrio_x))
else:
    print('Não foi possível encontrar o ponto de equilíbrio.')