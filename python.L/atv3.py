print("LEITURA DE NOTA")
print(" ")
nota = float(input("Digite sua nota: \n"))

if (nota < 0) or (nota > 100):
    print("NOTA INVÁLIDA ")
elif nota >= 60:
    print("APROVADO")
elif nota < 60:
    print("REPROVADO")