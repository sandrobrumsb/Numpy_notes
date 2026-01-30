"""
1. Ordenação de arrays com NumPy:

- Ordenar significa colocar elementos em uma sequência ordenada .
- O objeto ndarray do NumPy possui uma função chamada ` sort()sort`, que ordena um array especificado.

"""

# Exemplo - Ordene a matriz:

import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))  # Saída: [0 1 2 3]
# Observação: Este método retorna uma cópia da matriz, deixando a matriz original inalterada.

# Você também pode ordenar matrizes de strings ou qualquer outro tipo de dado:
# Exemplo - Ordene a matriz alfabeticamente:

import numpy as np

arr = np.array(["banana", "cherry", "apple"])
print(np.sort(arr))  # ['apple' 'banana' 'cherry']

# Exemplo - Ordenar um array booleano:
import numpy as np

arr = np.array([True, False, True])
print(np.sort(arr))  # [False  True  True]

# 2. Ordenando uma matriz bidimensional:
"""Se você usar o método sort() em uma matriz bidimensional, ambas as matrizes serão ordenadas"""
# Exemplo - Ordenar uma matriz bidimensional:
import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
