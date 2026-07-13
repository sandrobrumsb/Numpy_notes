"""
# 1. Dividindo arrays NumPy:
 - A divisão é a operação inversa da junção.
 - A operação de divisão (splitting) divide um array em vários outros.
 - Usamos essa função array_split()para dividir arrays
 - Passamos a ela o array que queremos dividir e o número de divisões.
"""

# Exemplo - Divida a matriz em 3 partes:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)  # Saída: [array([1, 2]), array([3, 4]), array([5, 6])]
# Observação: O valor retornado é uma lista contendo três arrays.

# Se a matriz tiver menos elementos do que o necessário, ela se ajustará a partir do final:
# Exemplo - Divida a matriz em 4 partes:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)  # Saída: [array([1, 2]), array([3, 4]), array([5]), array([6])]

"""
Observação: Também temos o método split()disponível, mas ele não ajustará os elementos quando houver poucos elementos na matriz de origem para divisão, como no exemplo acima; array_split()funcionou corretamente, mas split()falharia.
"""

# 2. Dividir em matrizes:
# Exemplo - Acesse os arrays divididos:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])


# 3. Divisão de matrizes bidimensionais:
# Utilize o método array_split(), passe o array que deseja dividir e o número de divisões que deseja realizar.
# Exemplo - Divida a matriz 2D em três matrizes 2D:
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

# OBS: O exemplo acima retorna três matrizes bidimensionais.

# Exemplo - Divida a matriz 2D em três matrizes 2D:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

# OBS: O exemplo acima retorna três matrizes bidimensionais.

# 4. Além disso, você pode especificar em torno de qual eixo deseja fazer a divisão.
# Exemplo - Divida a matriz 2D em três matrizes 2D ao longo das colunas.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

# Uma solução alternativa é usar hsplit()o oposto de hstack():
# Exemplo - Utilize o hsplit()método para dividir a matriz 2D em três matrizes 2D ao longo das colunas.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)

# OBS: Alternativas semelhantes a vstack()e dstack()estão disponíveis como vsplit()e dsplit().
