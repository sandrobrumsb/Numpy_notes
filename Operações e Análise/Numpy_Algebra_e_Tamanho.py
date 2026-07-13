"""
1. Tamanho de um objeto na memoria Python:
 - Cada número é um objeto Python.
 - Guarda: valor, tipo, contagem de referências.
 -
"""

# Exemplo:
import sys

print(sys.getsizeof(1))  # saida :  28 (bytes)

"""
1.1 NumPy usa arrays contíguos em memória.
 - Tipos fixos (int32, float64, etc.) 
 - Sem objetos Python por elemento.
 - NumPy usa muito menos memória para grandes volumes de dados.
"""
# Exemplo:
import numpy as np

a = np.array([1], dtype=np.int32)
print(a.nbytes)  # 4 bytes


"""
2. Tempo de execução:
 - Python puro: Loops executados no interpretador, 
 - lento para operações repetitivas.
"""
# Exemplo:
soma = 0
for i in range(1_000_000):
    soma += i
print(soma)

"""
2.2 NumPy:
  - Operações vetorizadas
  - Executadas em C otimizado
  - Menos overhead de loop em Python
  - Pode ser 10x a 100x mais rápido, dependendo da operação.
"""
# Exemplo:
import numpy as np

soma = np.sum(np.arange(1_000_000))
print(soma)

"""
3. Quando usar cada um:
 - Use Python puro quando:
    - Poucos dados.
    - Lógica complexa.
    - Código simples e legível.

- Use NumPy quando:
 - Grandes volumes de dados.
 - Cálculo numérico.
 - Operações repetitivas ou vetorizáveis.
 
"""
