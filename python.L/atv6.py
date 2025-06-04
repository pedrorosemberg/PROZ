print("SALÁRIO - FINANCIAMENTO")
print(" ")

salario = float(input("Informe seu salário:\n R$ "))
financiamento = float(input("Informe o valor de empréstimo desejado:\n R$ "))
soma = salario * 5

if financiamento <= soma:
    print("Financiamento concedido!")
else:
    print("Financiamento não concedido!")
