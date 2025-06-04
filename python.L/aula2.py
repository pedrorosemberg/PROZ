def obter_numero():
    while True:
        try:
            # Tenta converter o valor digitado para um inteiro
            numero = int(input("Digite um número inteiro: "))
            return numero  # Se a conversão for bem-sucedida, retorna o número
        except ValueError:
            # Caso o usuário digite algo que não pode ser convertido para int
            print("Isso não é um número válido! Tente novamente.")
        except Exception as e:
            # Captura outros erros inesperados
            print(f"Ocorreu um erro inesperado: {e}")
        finally:
            # Opcional: algo que você sempre quer fazer, como mostrar uma mensagem
            print("Tentando novamente...")

# Chama a função
numero = obter_numero()
print(f"Você digitou o número: {numero}")