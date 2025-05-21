# Este progama recebe tres numeros inteiros e mostra :
# O maior numero, o menor numero ea media dos dois numeros :

# Solicita ao usario os tre numeros a serem digitados;
num1 = int (input("DIGITE O PRIMEIRO NUMERO: "))
num2 = int (input("DIGITE O SEGUNDO NUMERO: "))
num3 = int (input("DIGITE O TERCEIRO NUMERO: "))

# Verificar qual e o maior numero entre os tres.
if (num1 > num2 ) and (num1 > num3):
    maior = num1
elif (num2 > num1) and (num2 > num3):
    maior = num2
else: 
    maior = num3

# Verificar qual e o menor numero entre os tres. 
if (num1 < num2) and (num1 < num3) : 
    menor = num1
elif (num2 < num1) and (num2 < num3) :
    menor = num2
else:
    menor = num3


    # calcula a media dos tres numeros. 

media = (num1 + num2 + num3) / 3

print ("o maior numero e", maior)
print ("o menor numero e ", menor)
print ("a media dos numeros e", media)


