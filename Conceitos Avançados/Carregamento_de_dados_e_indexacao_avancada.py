import numpy as np

"""
Carregar dados de um arquivo:
# Lê o arquivo "data.txt" localizado na pasta "./data/"
# O parâmetro delimiter=',' informa que os valores estão separados por vírgulas.

# Converte todos os valores do array para o tipo inteiro de 32 bits (int32).
# Isso é útil quando os dados representam números inteiros.

"""
filedata = np.genfromtxt("./data/data.txt", delimiter=",")
filedata = filedata.astype("int32")
print(filedata)  # Exibe o conteúdo do array no terminal.

"""
Mascaramento booleano e indexação avançada:
# Cria uma máscara booleana para verificar quais valores
# são maiores que 50 E menores que 100.
"""
print((~((filedata > 50) & (filedata < 100))))

"""
# Cria uma máscara booleana verificando quais elementos
# do array são maiores que 50.
# Em seguida, usa essa máscara para filtrar o array,
# retornando apenas os valores que satisfazem a condição.
"""
print(filedata[filedata > 50])
