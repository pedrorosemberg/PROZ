#define uma funcao cha,afa retorna_soma 
#que recebe dois parâmetros 
def retorna_soma(a,b):
    #retorna a soma dos dois paâmetros 
    return a + b

#início do programa principal
#solicita ao usuário que digite dois valores inteiros 
print("digite dois valores:")

#lê o primeiro valor e converte para inteiro
valor1 = int(input())

 #lê o segundo valor e converte para inteiro 
valor2 = int(input())

#chama a funçao retorna_soma passando os valores digitados 
#como argumentos 
resultado = retorna_soma(valor1, valor2)
print ("o resultado da sima é:",resultado)