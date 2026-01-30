"""
1. Filtragem de Matrizes
 - Extrair alguns elementos de uma matriz existente e criar uma nova matriz a partir deles é chamado de filtragem.
 - Em NumPy, você filtra uma matriz usando uma lista de índices booleanos .
 - Uma lista de índices booleanos é uma lista de valores booleanos correspondentes aos índices de um array.
 - Se o valor em um índice for verdadeiro, Trueo elemento está contido na matriz filtrada; caso contrário, Falseo elemento está excluído da matriz filtrada.
"""

# Exemplo - Crie uma matriz com os elementos nos índices 0 e 2:
import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]

print(newarr)  # [41 43]

# 2. Criando a matriz de filtro:
# O uso comum é criar uma matriz de filtro com base em condições.
# Exemplo - Crie um array de filtro que retorne apenas valores maiores que 42:
import numpy as np

arr = np.array([41, 42, 43, 44])

# Criando uma lista vazia
filter_arr = []

# percorra cada elemento em arr:
for element in arr:
    # Se o elemento for maior que 42, defina o valor como Verdadeiro, caso contrário, como Falso:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)  # [False, False, True, True]
print(newarr)  # [43 44]


# Exemplo - Crie um filtro que retorne apenas os elementos pares do array original:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Criando uma lista vazia
filter_arr = []

# percorra cada elemento em arr
for element in arr:
    # Se o elemento for completamente divisível por 2, defina o valor como Verdadeiro; caso contrário, defina como Falso.
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)  # [False, True, False, True, False, True, False]
print(newarr)  # [2 4 6]


# 3. Criando filtro diretamente a partir de um array:
# O exemplo acima é uma tarefa bastante comum em NumPy, e o NumPy oferece uma maneira interessante de lidar com ela.
# Podemos substituir diretamente a variável iterável pelo array em nossa condição e funcionará exatamente como esperamos.

# Exemplo - Crie um array de filtro que retorne apenas valores maiores que 42:
import numpy as np

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]

print(filter_arr)  # [False False  True  True]
print(newarr)  # [43 44]

# Exemplo - Crie um filtro que retorne apenas os elementos pares do array original:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]

print(filter_arr)  # [False  True False  True False  True False]
print(newarr)  # [2 4 6]
