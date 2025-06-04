print("Mês do ano")
print(" ")

dm = int(input("Digite o número do mês: "))
mes = ["janeiro", "fevereiro", "Março", "Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

if 1 <= dm <= 12:
        print("O mês é:", mes[dm - 1])
else:
        print("Mês inválido")