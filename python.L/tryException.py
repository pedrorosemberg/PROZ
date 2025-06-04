# ni = int(input("Digite o número inicial: "))
# nf = int(input("Digite o número final: "))
# if ni <= nf:
#     for numero in range(ni, nf + 1):
#         print(numero)
# else:
#     print("O número inicial deve ser menor ou ihual ao número final.")

opcao = -1

while True:
    print("-------------------")
    print("1 - Dizer olá!")
    print("2 - Dizer oi!")
    print("0 - Sair do programa")
    print("-------------------")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Invalid option. Try input a number...")
    else:
        if opcao == 1:
            print("Olá!")
        elif opcao == 2:
            print("Oi!")
        elif opcao == 0:
            print("Saindo do programa...")
        else:
            print("Invalid option. Try again later.")
    if opcao == 0:
        break
