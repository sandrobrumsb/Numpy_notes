"""
1 . Remodelando matrizes
 - Remodelar significa alterar o formato de uma matriz.
 - Ao remodelar, podemos adicionar ou remover dimensões ou alterar o número de elementos em cada dimensão.

"""

# Remodelar de 1D para 2D:
# Exemplo - Converta a seguinte matriz unidimensional com 12 elementos em uma matriz bidimensional.
# A dimensão mais externa terá 4 matrizes, cada uma com 3 elementos:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

# 2.Remodelar de 1D para 3D:
# Exemplo - Converta a seguinte matriz unidimensional com 12 elementos em uma matriz tridimensional.
# A dimensão mais externa terá 2 matrizes que contêm 3 matrizes, cada uma com 2 elementos:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)


# 3. Podemos nos transformar em qualquer forma?
# R: Sim, desde que os elementos necessários para a remodelação sejam iguais em ambas as formas.
"""
Podemos remodelar uma matriz 1D de 8 elementos em uma matriz 2D de 4 elementos em 2 linhas, mas não podemos remodelá-la em uma matriz 2D de 3 elementos em 3 linhas, pois isso exigiria 3x3 = 9 elementos.
"""
# Exemplo - Tente converter uma matriz unidimensional com 8 elementos, em uma matriz bidimensional com 3 elementos em cada dimensão (isso gerará um erro):
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(3, 3)
print(newarr)

# 4 - Retorna uma cópia ou uma visualização?
# Exemplo - Verifique se a matriz retornada é uma cópia ou uma visualização:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)
# O exemplo acima retorna o array original, portanto é uma visualização.

# 5 -Dimensão desconhecida:
# É permitido ter uma dimensão "desconhecida". Significa que você não precisa especificar um número exato para uma das dimensões no método reshape.

# Exemplo - Converter um array unidimensional com 8 elementos em um array tridimensional com 2x2 elementos:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

# 6. Aplanando as matrizes:
# Aplanar um array significa converter um array multidimensional em um array unidimensional.
# Podemos usar isso reshape(-1).

# Exemplo - Converter a matriz em uma matriz unidimensional:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
