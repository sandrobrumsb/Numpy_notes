"""
Formato do array NumPy:
 - O formato de uma matriz é determinado pelo número de elementos em cada dimensão.
"""

# 1. Obter o formato de uma matriz:
# Os arrays NumPy possuem um atributo chamado 'shape',
# que retorna uma tupla onde cada índice contém o número de elementos correspondentes.

# Exemplo - Imprima o formato de uma matriz bidimensional:
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)  # Saída: (2, 4)

# Significa que a matriz tem 2 dimensões, onde a primeira dimensão tem 2 elementos e a segunda tem 4.


# Exemplo - Crie uma matriz com 5 dimensões, usando ndmin, um vetor com os valores 1, 2, 3 e 4,
#  e verifique se a última dimensão tem o valor 4:
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)  # Saída: [[[[[1 2 3 4]]]]]
print("forma do array :", arr.shape)  # forma do array : (1, 1, 1, 1, 4)

# Isso significa: cada dimensao tem 1 elemento e a 5ª dimensao tem 4 elemento.
# ndmin=5 força o array a ter 5 dimensões
# Os dados reais continuam sendo [1, 2, 3, 4]
