import random

# .split() funciona para reconhecer e separar palavras 
entrada = input ("digite as palavras separadas por espaço:").split()

if entrada:

    palavra_aleatoria = random.choice(entrada)

#o (f) funcuona para reconhecer a variavel que se introduzira no meio da frase
    print(f"a palavra alaatoria é:{palavra_aleatoria}")

else:
     
     print("nenhuma palavra digitada,")
