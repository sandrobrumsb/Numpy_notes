- O que é NumPy?

* NumPy é uma biblioteca Python usada para trabalhar com arrays.
* NumPy significa Python Numérico.

- Por que usar NumPy?

* Em Python, temos listas que servem ao propósito de arrays, mas seu processamento é lento.
* O NumPy tem como objetivo fornecer um objeto de array que seja até 50 vezes mais rápido do que as listas tradicionais do Python.
* O objeto array no NumPy é chamado de array ndarraye fornece muitas funções auxiliares que ndarray facilitam bastante o trabalho com ele.
* Os arrays são usados ​​com muita frequência em ciência de dados, onde velocidade e recursos são muito importantes.
* Ciência de Dados: é um ramo da ciência da computação onde estudamos como armazenar, usar e analisar dados para extrair informações deles.

- Por que o NumPy é mais rápido que as listas?

* Diferentemente das listas, os arrays NumPy são armazenados em um único local contínuo na memória, permitindo que os processos acessem e manipulem esses arrays de forma muito eficiente.
* Esse comportamento é chamado de localidade de referência em ciência da computação.
* Essa é a principal razão pela qual o NumPy é mais rápido que listas. Além disso, ele é otimizado para funcionar com as arquiteturas de CPU mais recentes.

- Em que linguagem o NumPy foi escrito?

* NumPy é uma biblioteca Python, escrita parcialmente em Python, mas a maior parte das funcionalidades que exigem computação rápida são escritas em C ou C++.

---

# Instalação do NumPy:

- Se você já tiver o Python e o PIP instalados no sistema, a instalação do NumPy é muito fácil. Instale-o usando este comando:

```
pip install numpy

```

- Após instalar o NumPy, importe-o:

```
import numpy

```

- Agora o NumPy está importado e pronto para uso.
- OBS: O NumPy geralmente é importado sob o apelido "np".

```
import numpy as np
```

- Verificando a versão do NumPy:

```
import numpy as np

print(np.__version__
```


