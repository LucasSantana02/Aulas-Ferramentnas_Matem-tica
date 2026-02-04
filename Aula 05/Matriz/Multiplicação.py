from numpy import array, matmul
from sympy import Matrix, pprint

x = array([[3,1,3],[6,5,5]])
y = array([[100,50],[50,100],[50,50]])

z = matmul(x,y)
pprint(Matrix(z))