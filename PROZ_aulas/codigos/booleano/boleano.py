# Criamos uma lista de tamanho 4.
#Os elementos serão booleanos.

#inicia a lista com 4 elementos false.
vetorDeLogico = [False] *4

#Atribui o valor booleano true
#à primeira posição da lista (índice 0)
vetorDeLogico[0] = True

#usamos F-strings para formatar a saída, inserindo o 
#valor da variável.
print(f"Na posição 0, o valor é.: {vetorDeLogico[0]}")
print(f"Na posição 1, o valor é.: {vetorDeLogico[1]}")
print(f"Na posição 2, o valor é.: {vetorDeLogico[2]}")
print(f"Na posição 3, o valor é.: {vetorDeLogico[3]}")
