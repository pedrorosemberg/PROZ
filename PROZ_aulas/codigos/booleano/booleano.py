#inicializamos listas com zeros para definir o tamanho
NOME = [0] *3 
IDADE = [0] *3
# a viriavel 'cont' é usada como índice para percorrer 
#as listas.
cont = 0
#Loop 'for' em python que intera de 0 até 2 (inclusive).
for cont in range(3):
    #Imprime o cabeçalho de cadastro, encrementando 'cont'
    #Para exibir o número do cadastro.
    print(f"---- {cont + 1}°-cadastro ---------")
    print ()
    # Solicita e lê o nome do usuario, armazenando-o na 
    #lista NOME na posição 'cont'.
    print ("Digite seu nome:")
    NOME[cont] = input()
    #solicita e lê a idade do usuário, convertendo a 
    #entrada para inteiro e armazenamento na lista IDADE.
    print("Digite seu idade:")
    IDADE[cont]= int(input())
    #Solicita e lê o telefone do usuário, armazenado-o
    #simula a limoeza da tela.
print("\n" * 20)
#outro loop 'for' para exibir os dados cadastrados. 
for cont in range(3):
    #imprime os dados de cada pessoa formados.
    print(f"Nome: {NOME[cont]}")
    print(f"Idade: {IDADE[cont]} anos")
    print("---------------------------------------")