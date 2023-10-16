#!C:/Python310/python.exe

"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Para ver qual a linha do SO Windows: env | grep LANG

Como usar:

Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR

Execução:

    python hello.py
    ou
    python3 hello.py
    ou
    ./hello.py - isso dá certo por conta do shebang, linha 1.

    Sobrescrevendo o valor de LANG do SO:
        LANG=it_IT ./hello.py
        ou
        LANG=pt_BR python hello.py
        ou
        LANG=es_SP python hello.py
        ou
        LANG=fr_FR python hello.py
"""

__version__ = "0.0.1"
__author__  = "Otto"
__license__ = "Unlicense"

import  os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)