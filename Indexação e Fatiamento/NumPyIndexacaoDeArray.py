# 1. Acessar elementos de matriz:
# Obtenha o primeiro elemento da seguinte matriz:

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[2])  # Saída: 3

# Obtenha o terceiro e o quarto elementos da seguinte matriz e some-os.

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[1] + arr[2])  # Saída: 5

# 2. Acesso a matrizes bidimensionais
# Acesse o elemento na primeira linha, segunda coluna:
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Primeiro elemento da primeira linha: ", arr[0, 0])  # Saída: 1
print("Segundo elemento da primeira linha: ", arr[0, 1])  # Saída: 2
print("Terceiro elemento da primeira linha: ", arr[0, 2])  # Saída: 3

# Acesse o elemento na segunda linha, quinta coluna:
print(arr[1, 4])  # Saída: 10

# 3. Acesso a matrizes 3D.
# Acesse o terceiro elemento da segunda matriz da primeira matriz:

import numpy as np

arr = np.array([[[1, 2, 3], 
                 [4, 5, 6]], 
                 [[7, 8, 9], 
                  [10, 11, 12]]])
# arr[bloco, linha, coluna]
print(arr[0, 1, 2]) # Saída: 6
print(arr[1,1,2])# Saída: 12

"""
Explicação: arr[0, 1, 2] [bloco, linha, coluna]
1 - O primeiro número representa os blocos (primeira dimensão), que contém dois arrays ou seja posição 0
2 - O segundo número representa as linhas(segunda dimensao), que também dos dois arrays iniciais ou seja posição 1
3 - O terceiro número representa a coluna (terceira dimensão), que contém três valores:
"""

# 4. Indexação negativa
# Use indexação negativa para acessar um array a partir do final.
# Imprima o último elemento da segunda dimensão:

import numpy as np

arr = np.array([[1,2,3,4,5], 
                [6,7,8,9,10]])
# arr[linha, coluna]
print('ultimo elemento da segunda dimensao: ', arr[1, -1]) # Saída: 10
print('Penultimo elemento da segunda dimensao: ', arr[1, -2]) # Saída: 09
print('ultimo elemento da primeira dimensao: ', arr[0, -1]) # Saída: 09