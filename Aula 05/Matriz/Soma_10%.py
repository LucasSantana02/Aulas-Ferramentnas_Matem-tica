import sympy as sp
import numpy as np 
F1=np.array([[3000, 110],[5000, 120],[6500, 125]]) 
F2=np.array([[300, 130],[350, 130],[420, 130]])
CustoTotal=(F1*1.1)+F2
print(' Matriz de Custo Total com 10% de aumento em F1:')
sp.pprint(sp.Matrix(CustoTotal))