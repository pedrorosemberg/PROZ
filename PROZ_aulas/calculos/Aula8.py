avaliacoes = []
for i in range(3):
    print(f"\n-----Cadastro de Usuario----- {i + 1}")
    nome = input("Digite o seu nome:")
    filme = input("Digite o nome do filme que assistiu:")

    while True:
        try:
            nota = float(input("Digite uma nota para o filme de 0 a 10: "))
            if 0 < nota > 10:
                break
            else:
                print("Nota invalída. Digite uma nota entre os numeros 0 e 10.")
        except ValueError:
            print("Valor invalído! Digite outro número.")
              
avaliacoes.append([nome, filme, nota])

print("\n-----Resultado Final-----")

for avaliacao in avaliacoes:
    print(f"{avaliacao[0]} | Filme assistido: {avaliacao[1]} | Nota: {avaliacao[2]}")