import numpy as np
import sympy as sp
arc = np.deg2rad(30)
sen = np.sin(arc)

arco = sp.rad(30) # Converte graus para radianos de forma exata (pi/6)
seno = sp.sin(arco)
sp.pprint(seno)
sp.pprint(sen)  # Valor numérico aproximado