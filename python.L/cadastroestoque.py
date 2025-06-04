
print("cadastro de produtos de estoque")

# programas para ajudar a controlar os produtos de uma loja

produto = ""     # o programa deve permitir que o usuario cadastre varios produtos
estoque = -1     # informando: o nome do produto
total = 0        # a quantidade  de produto em estoque
soma = 0

while True: c

    # o nome do produto em estoque
   nome = input("\ndigite o nome do produto em estoque:")

# soma total das quantidades
estoque_str = input("digite a quantidade de produto em estoque:")

# validar a entrada com .isdjit() para garantir que a quantidade seja numerica.
if produto_str.isdjit():
    estoque = int(estoque_str)
else:
     print("quantidade invalido.digite apenas numeros.")
     continue
     
    total  =+ 1
    quantidade += estoque
if 
    quantidade < mais_estoque_quantidade:
    mais_estoque_quantidade = quantidade
    mais-estoque_produto = produto

        continuar = input("deseja continuar? (S/N):").strip().upper()
        
 if  continuar != 'S':
        break

#exibe o resultado final
print("\resultado final:")
print(f"total de produtos cadastrado:{total}")
print(f"media de quantidade do estoque:{soma/total:.1f}numero*)
print(f"produtos cadastrados:{mais_produto_estoque}({mais_produto_cadastrado}numero*)")