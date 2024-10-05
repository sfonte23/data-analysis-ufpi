# Exercício: Crie um vetor de 10 elementos aleatórios, calcule a média, mediana e o desvio padrão.

import numpy as np

# Criando um vetor de 10 elementos aleatórios
vetor_aleatorio = np.random.rand(10)

# Cálculo da média, mediana e desvio padrão
media = np.mean(vetor_aleatorio)
mediana = np.median(vetor_aleatorio)
desvio_padrao = np.std(vetor_aleatorio)

print("Vetor Aleatório:", vetor_aleatorio)
print("Média:", media)
print("Mediana:", mediana)
print("Desvio Padrão:", desvio_padrao)
