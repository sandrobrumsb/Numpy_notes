"""
1. Iterando Matrizes:
 - Iterar significa analisar os elementos um por um.
 - Ao lidarmos com arrays multidimensionais no NumPy, podemos fazer isso usando um loop for básico do Python.
 - Se iterarmos sobre uma matriz unidimensional, percorreremos cada elemento um por um.
"""

# Exemplo - pecorra sobre os elementos da seguinte matriz unidimensional:
import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
    print(x)

# 2. Iteração de matrizes bidimensionais:
# Em uma matriz bidimensional, ele percorrerá todas as linhas.
# Exemplo - pecorra sobre os elementos da seguinte matriz bidimensional:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)

# Exemplo - pecorra sobre cada elemento escalar da matriz bidimensional:
# Ele ira percorre a matriz inteira e mostra cada número individualmente.
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)


# Iteração de matrizes 3D:
# Em uma matriz 3D, ele percorrerá todas as matrizes 2D.
# Exemplo - pecorra sobre os elementos da seguinte matriz tridimensional:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print(x)

# Para retornar os valores reais, os escalares, precisamos iterar pelos arrays em cada dimensão.
# Exemplo - Itere até chegar aos escalares:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)

# 3.Iterando arrays usando nditer()
"""
Essa função nditer()é uma função auxiliar que pode ser usada desde iterações muito básicas até as mais avançadas.
Ela resolve alguns problemas básicos que enfrentamos em iterações

Iterando em cada elemento escalar:
Em forloops básicos, ao iterar por cada elemento escalar de um array, precisamos usar n for loops, o que pode ser difícil de escrever para arrays com dimensionalidade muito alta.
"""
# Exemplo - Percorra a seguinte matriz tridimensional:
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)


# 4. Iterando um array com diferentes tipos de dados:
"""
Podemos usar op_dtypeso e passar o tipo de dados esperado para alterar o tipo de dados dos elementos durante a iteração.

O NumPy não altera o tipo de dados do elemento no local (onde o elemento está no array), então ele precisa de algum espaço extra para realizar essa ação; esse espaço extra é chamado de buffer, e para habilitá-lo, passamos o nditer() flags=['buffered'].
"""
# Exemplo - Esse trecho cria um array NumPy e percorre ele convertendo cada elemento para string (bytes).
import numpy as np

arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
    print(x)

# 5. Iteração com diferentes tamanhos de passo:
# Exemplo - Percorra cada elemento escalar da matriz 2D, pulando 1 elemento:
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
    print(x)

# 6. Iteração enumerada usando ndenumerate()
# Exemplo - percorre cada array do NumPy e imprime, para cada elemento, o índice e o valor correspondente:
import numpy as np

arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

  """
Saida:
(0,) 1
(1,) 2
(2,) 3
  """

# Exemplo - Enumere os seguintes elementos da matriz 2D:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

  """
saida:
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8

  """

  