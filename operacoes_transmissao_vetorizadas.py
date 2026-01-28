# O nunpy é uma biblioteca imutavel, qualquer operação que eu fizer 
# nao modificara o array ,mas sim retornara um novo array.

# 1. somando os elementos do array com um numero, EX:
import numpy as np

arr = np.array([1, 2, 3])
print(arr + 10)  # Saída: [11 12 13]

# 2. Subtraindo um número dos elementos do array:
import numpy as np

arr = np.array([1, 2, 3])
print(arr - 5)  # Saída: [-4 -3 -2]


# multiplicando:
import numpy as np

arr = np.array([1, 2, 3])
print(arr * 10)  # Saída: [10 20 30]

# 3. Dividindo os elementos do array por um número:
import numpy as np

arr = np.array([10, 20, 30])
print(arr / 5)  # Saída: [2. 4. 6.]

# 4. Elevando os elementos do array a uma potência (ex: quadrado):
import numpy as np

arr = np.array([1, 2, 3])
print(arr**2)  # Saída: [1 4 9]

# 5. Operações entre dois arrays (elemento a elemento):
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])
print(arr1 + arr2)  # Saída: [11 22 33]
print(arr1 * arr2)  # Saída: [10 40 90]
print(arr1 / arr2)  # Saída: [0.1 0.1 0.1]

# 6. Comparando os elementos de um array com um número (resultado booleano):
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr > 3)  # Saída: [False False False  True  True]

# 7. Soma de todos os elementos de um array:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))  # Saída: 15

# 8. Média de todos os elementos de um array:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))  # Saída: 3.0

# 9. Concatenando arrays:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(np.concatenate([arr1, arr2]))  # Saída: [1 2 3 4 5 6]
