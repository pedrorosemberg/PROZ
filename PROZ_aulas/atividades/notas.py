# Programa para verificar se o aluno passou.

nota = float (input("DIGITE A NOTA (0 a 10):"))

while nota < 0 or nota > 10:

    print ("Erro! A NOTA TEM QUE SER ENTRE 0 A 10")

    nota = float (input("DIGITE A NOTA NOVAMENTE:"))

if nota >= 7:
    print ("ALUNO APROVADO!")

else:
    print ("ALUNO REPROVADO!")
    