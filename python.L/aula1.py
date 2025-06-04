def validar_nome(nome):
    if nome.isalpha():
       return True
    else:
       return False
def validar_idade(idade):
    if idade.isdigit():
       return True
    else:
       return False

nome = input("digite seu nome:")
idade = input("digite sua idade:")

    if validar_nome(nome):
     print("nome invalido")
    else:
     print("nome invvalido! o nome deve conter apenas letras")
    if validar_idade(idade):
        print("idade invalida")
    else:

     print("idade invalida! a idade deve ser um numero")


