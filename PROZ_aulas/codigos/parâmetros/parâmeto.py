#criando um procedimento com par^metro
#(em python, definimos uma funçao que aceita um argumento)
def saudacao(nomeUsuario):
    print (f"ola {nomeUsuario}")

#escreva ("digite o sei nome:")
print("digite seu nome:")

#lendo o nome do usuário
nome= input()

#saudaçao(nome)  //chamando um procedimento 
#                //e passando parâmetro 

saudacao(nome)