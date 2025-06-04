print("HORAS TRABALHADAS")
hr = int(input("Digite horas trabalhadas: \n"))
soma = 600 + (hr - 40)* 21
if hr <= 40: 
    print("Seu salário é de: R$", hr * 15)
elif hr >= 40:
    print("Seu salário é de: R$",soma)
