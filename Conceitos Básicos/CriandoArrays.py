import numpy as np

# 1. Criando um objeto ndarray do NumPy:
# O objeto array em NumPy é chamado de ndarray.
# Podemos criar um objeto ndarray usando uma função array():

arr = np.array([1, 2, 3, 4, 5])

print(arr)  # Resultado
print(type(arr))  # mostra o tipo que estamos usando.
print(np.__version__)  # mostra a versão do numpy.

# 2. Para criar um array ndarray, podemos passar uma lista, tupla ou qualquer objeto semelhante a um array para a classe array().
# Utilize uma tupla para criar um array NumPy:
import numpy as np

arr = np.array((1, 2, 3, 4, 5))
print(arr)
print(arr.dtype)  # saída: int64 | inteiro 64 bits

# Extraindo elementos especificos:
import numpy as np

a = np.array([1, 2, 3, 777, 5, "texto"])
b = np.array([0, 0.52, 1, 4.5, 10.5, "outro_texto"])

print(a[3])  # saída: 777
print(a[2:5])  # saída: ['3' '777' '5']
print(b[5])  # saída: outro_texto
print(b[3:])  # saída: ['4.5' '10.5' 'outro_texto']


# 3. Dimensões em arrays(matrizes):
# Uma dimensão em matrizes corresponde a um nível de profundidade da matriz (matrizes aninhadas).
# 0-D Arrays ou escalares, são os elementos em um arrays. Cada valor em um arrays é um 0-D array.
# Exemplo - Crie um 0-D array com o valor 42:
import numpy as np

arr = np.array(42)
print(arr)

# 1-D Arrays - Matrizes unidimensionais:
# Uma Array que possui 0-D como seus elementos é chamada de matriz unidimensional ou 1-D Arrays.
# Exemplo: Criando a 1-D array contendo os valores  1,2,3,4,5:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2-D Arrays - Matrizes bidimensionais:
# Uma Array que possui matrizes unidimensionais como elementos é chamada de Array bidimensional.
# Esses elementos são frequentemente usados ​​para representar Arrays ou tensores(tensor) de segunda ordem.
# Exemplo: Crie uma array bidimensional contendo dois arrays com os valores 1,2,3 e 4,5,6:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.shape)  # saída:(2,3) | mostra a dimensao desse array = 2 linhas e 3 colunas

# obs: Esse array possui 2 dimensoes 1 vertical e 1 horizontal.

print(arr.size)  # saída: 6 | tamanho total dessa matriz.

# substituindo todos os elementos dessa linha no array na posição [1] da dimensao:
arr[1] = np.array([7, 8, 9])
print(arr) # Saída[1 2 3] [7 8 9]

arr[1] = 99  # substituindo todos os elementos para 99 do array na posição [1]
print(arr)  # Saída: [1 2 3] [99 99 99]


# 3-D arrays - Um array que possui elementos compostos por array bidimensionais é chamada de matriz tridimensional.
# Esses elementos são frequentemente usados ​​para representar um tensor de terceira ordem.
# Exemplo - Crie um array 3D com dois arrays 2D, ambas contendo dois array com os valores 1,2,3 e 4,5,6:
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)  # Saída: Resultado do array 3D
print(
    arr.shape
)  # Saída: (2, 2, 3) | Dimensões do array (2 blocos, 2 linhas e 3 colunas)
print(arr.ndim)  # Saída: 3 | número de dimensões
print(arr.size)  # Saída: 12 | Mostra o total de elementos(2 × 2 × 3 = 12)
print(arr[0])  # Saída: [1 2 3] [4 5 6] | Extraindo dimensoes especificas.
print(
    arr[1]
)  # Saída: [7  8  9] [10 11 12] | Extraindo dimensoes especificas(2ªdimensai).

# Extraindo elementos de dimensoes especificas:
print(arr[0, 1, 2])  # Saída: 6
print(arr[1, 1, 2])  # Saída: 12


# 4. Verificar o número de dimensões?
# Os arrays NumPy fornecem um atributo "ndim" que retorna um número inteiro indicando quantas dimensões o array possui.
# Exemplo - Verifique quantas dimensões as matrizes possuem:
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# 5. Matrizes de Dimensão Superior:
# Um array pode ter qualquer número de dimensões.
# Ao criar o array, você pode definir o número de dimensões usando o argumento "ndmin":
# Exemplo - Crie uma matriz com 5 dimensões e verifique se ela realmente possui 5 dimensões:

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)  # definindo a quantidade de dimensões.
print(arr)
print("numero de dimensoes: ", arr.ndim)


# 6. summary statistics | estatísticas resumidas:
import numpy as np
arr = np.array([1, 2, 3, 4])

print(arr.sum())      # Saída: 10 | Soma todos os elementos do array (1+2+3+4)
print(arr.mean())     # Saída: 2.5 | Calcula a média aritmética dos elementos
print(arr.max())      # Saída: 4 | Maior valor do array
print(arr.min())      # Saída: 1 | Menor valor do array
print(arr.argmax())   # Saída: 3 | Indice do maior valor (4 está na posição 3)
print(arr.argmin())   # Saída: 0 | Indice do menor valor (1 está na posição 0)
print(arr.std())      # Saída: 1.118033988749895 | Desvio padrão, mostra dispersão dos valores
print(arr.var())      # Saída: 1.25 | Variância, quadrado do desvio padrão
print(arr.cumsum())   # Saída: [1 3 6 10] | Soma cumulativa dos elementos
