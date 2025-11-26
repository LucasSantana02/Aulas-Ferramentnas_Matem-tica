diametro = 84728
min = 0.054
max = 0.079
diametro_min = diametro * min
diametro_min = round(diametro_min, 2)
diametro_max = diametro * max
diametro_max = round(diametro_max, 2)
print('Diametro mínimo do cilindro é:', diametro_min)
print('Diametro máximo do cilindro é:', diametro_max)
print('Tolerância do diâmetro é de:', round(diametro_max - diametro_min, 2))
#Os componentes de um vetor em 3D