"""
1. NumPy Array Slicing:

 - Em Python, "slicing" significa extrair elementos de um índice dado para outro índice dado.
 - Extraimos o índice desta forma: .[start:end]
 - Também podemos assim: .[start:end:step]

"""

# Exemplo - Extraia os elementos do índice 1 ao índice 5 da seguinte matriz:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])  # Saída: [2 3 4 5]
# Observação: O resultado inclui o índice inicial, mas exclui o índice final.

# Exemplo - Extraia os elementos apartir índice 4 até o final da matriz:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])  # Saída: [5 6 7]

# Exemplo - Extraia os elementos do início até o índice 4 (não incluído):
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])  # Saída: [1 2 3 4]


"""
2. Fatiamento negativo
 - Use o operador de menos (-) para se referir a um índice a partir do final.

"""
# Exemplo - Corte do índice 3 a partir do final até o índice 1 a partir do final:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])  # Saída: [5 6]

"""
3. ETAPA
    - Utilize o stepvalor para determinar o passo do fatiamento
"""
# Exemplo - Retorne todos os elementos do índice 1 ao índice 5:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])  # Saída: [2 4]
# OBS: do índice 1 ao 4, pegue os elementos de 2 em 2.

# Exemplo - Retorne todos os outros elementos da matriz:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])  # Saída: [1 3 5 7]
# OBS: do índice 0 ao 6, somente os elementos de 2 em 2.


"""
4 . Fatiamento de matrizes bidimensionais
"""
# Exemplo - A partir do segundo elemento, extraia os elementos do índice 1 ao índice 4 (não incluído):

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])  # Saída: [7 8 9]
# OBS: Acessa o segundo array, que é o indice [1] da matriz, em seguida os elementos dos indices [1],[2] e [3] desse array.

# Outro exemplo:
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, "branco", "preto", "cinza", 10]])
print(arr[1, 1:4])  # Saída: ['branco' 'preto' 'cinza']

# Exemplo -  A partir de ambos os elementos, retorne o índice 2:
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])  # Saída: [3 8]
# Obs: pega a 3ª coluna (índice 2) de todas as linhas do array.


# Exemplo - A partir de ambos os elementos, extraindo do índice 1 ao índice 4 (não incluído esse indice 4),
# obteremos uma matriz bidimensional:
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])  # Saída: [[2 3 4],[7 8 9]]
