print ("digite o seu nome:")
nome = input ()

def pagamento (a,b):
    return a * b

print ("digite as horas de trabalhos:")

horas = float(input())

print ("digite o valor da hora:")

valor = float(input())

resultado = pagamento (horas, valor)
print ("olá",nome,"o valor a ser pago para você é:", resultado)

