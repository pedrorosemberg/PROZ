print("CALCULO DE IDADE")
print(" ")

at = int(input("Digite o ano atual: \n"))
an = int(input("Digite seu ano de nascimento: \n"))

idade = at - an

print(" ")
print("Sua idade é: ", idade)

if idade <= 3:
    print("Você é considerado bebê!")
elif idade >= 4 and idade <= 10:
    print("Você é considerado criança")
elif idade >= 11 and idade <= 18:
    print("Você é considerado adolescente")
elif idade >= 19 and idade <= 50:
    print("Você é considerado adulto")
elif idade >= 51:
    print("Você é considerado idoso")
