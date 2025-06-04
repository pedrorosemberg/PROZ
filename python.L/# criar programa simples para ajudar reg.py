# criar programa simples para ajudar registrarr informação de uma turma.

print("cadastro de alunos e notas")

aluno = "" 
nota = -1
total = 0
soma = 0

while True: 

    
   aluno = input("\ndigite o nome do aluno:")
   nota = float(input("digite a nota do aluno: "))


# validar a entrada com .isdjit() para garantir que a quantidade seja numerica.
if nome_str.isdjit():
    nota = int(nota_str)
else:
     print("nota invalido.digite apenas numeros.")
     
     
    aluno  =+ 1
    nome += nota  
    
if  aluno < mais_notas_notas:
    mais_aluno_notas = notas
    mais-aluno_nome = nome

      continuar= input("deseja continuar? (S/N):").strip().upper()
        
 if  continuar != 'S':
        break

#exibe o resultado final
print("\resultado final:")
print(f"nome do aluno cadastrado:{nome}")
print(f"media da nota do aluno:{soma/total:.1f}nome*)
print(f"notas cadastradas:{mais_nome_nome}({mais_notas_cadastradaso}notas*)")