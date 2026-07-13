"""
1. Tipos de dados em NumPy:
 - NumPy possui alguns tipos de dados extras e se refere,
   a tipos de dados com um único caractere, como `int` ipara inteiros,
   u`unsigned integers` para inteiros sem sinal, etc.


i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V- bloco fixo de memória para outro tipo (void)
"""

# Verificando o tipo de dados de uma matriz:
# O objeto array do NumPy possui uma propriedade chamada 'dtype' que retorna o tipo de dados do array:
# Exemplo - Obtenha o tipo de dados de um objeto de matriz:
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)  #  saida: int64

# Exemplo - Obtenha o tipo de dados de uma matriz que contém strings:
import numpy as np

arr = np.array(["apple", "banana", "cherry"])
print(arr.dtype)  # Saida: <U6


# 2 . Criando matrizes com um tipo de dados definido

#  Exemplo - Crie uma matriz com o tipo de dados string:
import numpy as np

arr = np.array([1, 2, 3, 4], dtype="S")
print(arr)  # saída: [b'1' b'2' b'3' b'4']
print(arr.dtype)  # saída: |S1

# Exemplo - Crie um array com tipo de dados inteiro de 4 bytes:
import numpy as np

arr = np.array([1, 2, 3, 4], dtype="i4")
print(arr)  # saída: [1 2 3 4]
print(arr.dtype)  # saída: int32


# 3. E se um valor não puder ser convertido?
# Se for fornecido um tipo em que os elementos não podem ser convertidos, o NumPy lançará um erro ValueError.

# Exemplo - Uma string que não seja um número inteiro, como 'a', não pode ser convertida para um número inteiro (isso gerará um erro):
import numpy as np

arr = np.array(["a", "2", "3"], dtype="i")

# 4 .Convertendo o tipo de dados em matrizes existentes
# A melhor maneira de alterar o tipo de dados de um array existente é fazer uma cópia do array.
# A função astype() cria uma cópia da matriz e permite que você especifique o tipo de dados como um parâmetro.

# Exemplo - Alterar o tipo de dados de float para integer usando 'i'como valor do parâmetro:
import numpy as np

meu_array = np.array([1.1, 2.1, 3.1])

novo_array = meu_array.astype("i")
print(novo_array)  # Saída: [1 2 3]
print(novo_array.dtype)  # Saída: int32

# Exemplo - Alterar o tipo de dados de float para integer, usando "int" como valor do parâmetro:
import numpy as np

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)

print(newarr)  # Saída:  [1 2 3]
print(newarr.dtype)  # Saída: int64

# Exemplo - Alterar o tipo de dados de inteiro para booleano:
import numpy as np

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)

print(newarr)  # Saída: [ True False  True]
print(newarr.dtype)  # Saída: bool
