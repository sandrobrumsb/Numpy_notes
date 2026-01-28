"""
Cópia versus visualização de array NumPy:

A principal diferença entre uma cópia e uma visualização de um array é que a cópia é um novo array, enquanto a visualização é apenas uma representação do array original.

"""

# Exemplo - Faça uma cópia, altere a matriz original e exiba ambas as matrizes:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)


# VISUALIZAR:
# Exemplo - Crie uma visualização, altere a matriz original e exiba ambas as matrizes:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)  # Saída: [42  2  3  4  5]
print(x)  # Saída: [42  2  3  4  5]

# Faça alterações na VISUALIZAÇÃO:
# Exemplo - Crie uma visualização, altere a visualização e exiba ambas as matrizes:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)  # Saída: [31  2  3  4  5]
print(x)  # Saída: [31  2  3  4  5]

# Verifique se o array é proprietário dos seus dados:
# cópias são proprietárias dos dados, enquanto as visualizações não são proprietárias dos dados,

# Exemplo - Imprima o valor do atributo base para verificar se um array é proprietário dos seus dados ou não:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)  # Saída: None
print(y.base)  # Saída: [1 2 3 4 5]
# OBS: A cópia retorna None.| A visualização retorna o array original.

