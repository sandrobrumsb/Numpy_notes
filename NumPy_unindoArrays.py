"""
# 1. Unindo matrizes NumPy

"Unir" significa colocar o conteúdo de duas ou mais matrizes em uma única matriz.
 - Em SQL, unimos tabelas com base em uma chave, enquanto em NumPy unimos arrays por eixos.
 - Passamos para a função  concatenate() uma sequência de arrays que queremos unir, juntamente com o eixo. Se o eixo não for passado explicitamente, ele será considerado como 0.

"""

# Exemplo  - Unir duas matrizes:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)


# Una duas matrizes 2D ao longo das linhas (eixo=1):

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)


# 2 . Unindo matrizes usando funções de pilha:
"""
 - Empilhamento é o mesmo que concatenação, a única diferença é que o empilhamento é feito ao longo de um novo eixo.
 - Podemos concatenar duas matrizes unidimensionais ao longo do segundo eixo, o que resultaria em colocá-las uma sobre a outra, ou seja, empilhá-las.
 - Passamos para o método stack() uma sequência de arrays que queremos unir, juntamente com o eixo. Se o eixo não for passado explicitamente, ele será considerado como 0.  
"""
# Exemplo:

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)  # axis=1 → define como eles serão unidos

print(arr)

"""
obs: O que significa axis=1?
- Cada elemento de arr1 é colocado ao lado do elemento correspondente de arr2.
"""

# 3. Empilhamento ao longo de fileiras:
# O NumPy fornece uma função auxiliar: hstack() para empilhar ao longo das linhas.
# Exemplo:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)

# 4. Empilhamento ao longo de colunas:
# O NumPy fornece uma função auxiliar: vstack()  para empilhar ao longo das colunas.
# Exemplo:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))

print(arr)

# 5.Empilhamento ao longo da altura (profundidade):
# O NumPy fornece uma função auxiliar dstack() para empilhar ao longo da altura, que é o mesmo que a profundidade.
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))

print(arr)
