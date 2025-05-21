#difinindo a funçao "verificarsexo" que recebe a variavel 'sexo'
#como parâmetro
def verificarsexo(sexo):
    #verifica se o sexo é "f" para feminino
    if sexo == "f":
        #se for feminino, imprime "Feminino"
        print("feminino")
    else:
        #caso contrário, imprime "Masculino"
        print("masculino")

#solicita ao usuário para digitar seu sexo (f para feminino e m oara 
#masculino)
print("Digite o seu sexo: (f) para feminino e (m)para masculino:")

#lê a entrada do usuário e armazena na variável 'sexo'
sexo = input()

#chama a funcao 'verificarSexo' passando o valor de 'sexo'
verificarsexo(sexo)