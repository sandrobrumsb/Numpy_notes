# 1. Pesquisando em matrizes:
# Para pesquisar em um array, use o método where().

# Exemplo - Encontre os índices onde o valor é 4:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)  # Saída: (array([3, 5, 6]),)

#  Encontre os índices onde os valores são pares:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 0)
print(x)

# Encontre os índices onde os valores são ímpares:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 1)
print(x)

# 2. Pesquisa ordenada:
"""
Existe um método chamado 'earchsorted()' que realiza uma busca binária na matriz e retorna o índice onde o valor especificado seria inserido para manter a ordem da busca.
"""
# OBS: Presume-se que o searchsorted()método seja usado em arrays ordenados.

# Exemplo - Encontre os índices onde o valor 7 deve ser inserido:

import numpy as np

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

# Exemplo explicado: O número 7 deve ser inserido no índice 1 para manter a ordem de classificação.

# Pesquisar pelo lado direito, podemos especificar side='right'para que seja retornado o índice mais à direita.
# Exemplo -Encontre os índices onde o valor 7 deve ser inserido, começando da direita:

import numpy as np

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side="right")

print(x)
# Exemplo explicado: O número 7 deve ser inserido no índice 2 para manter a ordem de classificação.

# 3. Valores múltiplos:
# Para pesquisar mais de um valor, use uma matriz com os valores especificados.
# Exemplo - Encontre os índices onde os valores 2, 4 e 6 devem ser inseridos:

import numpy as np

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])

print(x)

# OBS: O valor retornado é uma matriz [1 2 3]contendo os três índices onde 2, 4 e 6 seriam inseridos na matriz original para manter a ordem.
