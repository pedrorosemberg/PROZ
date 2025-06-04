print("FUNDOS")
ano = int(input("Digite em meses a quanto tempo o dinheiro está mantido em depósito: "))
tempo = ano/12
print("Convertendo para ano: ", tempo, " ano")

if tempo >= 5:
 taxa = 0.95
elif tempo <= 5 and tempo >= 4:
 taxa = 0.90
elif tempo <= 4 and tempo >= 3:
  taxa = 0.85
elif tempo <= 3 and tempo >= 2:
  taxa = 0.75
elif tempo <= 2 and tempo >= 1:
  taxa = 0.65
elif tempo <= 1:
  taxa = 0.55

print("A taxa de juros pelo tempo é de: ", taxa)