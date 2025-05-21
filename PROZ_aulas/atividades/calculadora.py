#Este programa realiza operações básicas com dois números
#fonecidos pelo usuário.

num1 = float (input("DIGITE O PRIMEIRO NÚMERO:"))
num2 = float (input("DIGITE O SEGUNDO NÚMERO:"))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

if num2 != 0:
    divisao = num1 / num2

else:
    divisao = "Dividido por zero não é permitida."

media = (num1 + num2) / 2

print ("-------------RESULTADOS--------------")
print (f"SOMA: {soma}")
print (f"SUBTRAÇÃO: {subtracao}")
print (f"MULTIPLICAÇÃO: {multiplicacao}")
print (f"DIVISÃO: {divisao}")
print (f"MÉDIA: {media}")
print ("-------------------------------------")