# 1. Indexação booleana no NumPy:
# elecionar elementos do array com uma máscara booleana:
import numpy as np

arr = np.arange(4)  # [0 1 2 3]
print(arr[[True, True, False, True]])  # Saída: [0 1 3]

# 2. indexação booleana baseada em condição:
import numpy as np

arr = np.arange(4)  # [0 1 2 3]
print(arr[arr >= 2])  # Saída: [2 3]

# Exemplo 2:
arr = np.array([100, 250, 33, 4, 505, 200, 350, 450, 1000])
print(arr[arr <= 100])  # Saída: [100  33   4]
