#inicia uma lista de listas chamda MATRIZ para representar a ,etriz 4x4 
#cada lista interna representa uma linha da matriz, inicializada com 4 zeros  
matriz = [[0] * 4 for _ in range (4)]

#Preenche a linha de índice 0 da matriz:
#atribui o valor 0 ao elemento nal inha 0,coluna 0
matriz[0][0] = 0
#Atribui o valor 1 ao elemento na linha 0,coluna 1
matriz[0][1] = 1
#Atribui o valor 0 ao elemento da linha 0, coluna 2
matriz[0][2] = 0
#Atribui o valor 1 ao elemento da linha 0, coluna 3
matriz[0][3] = 1

matriz[1][0] = 0
#Atribui o valor 1 ao elemento na linha 0,coluna 1
matriz[1][1] = 0
#Atribui o valor 0 ao elemento da linha 0, coluna 2
matriz[1][2] = 1
#Atribui o valor 1 ao elemento da linha 0, coluna 3
matriz[1][3] = 0

matriz[2][0] = 1
#Atribui o valor 1 ao elemento na linha 0,coluna 1
matriz[2][1] = 1
#Atribui o valor 0 ao elemento da linha 0, coluna 2
matriz[2][2] = 1
#Atribui o valor 1 ao elemento da linha 0, coluna 3
matriz[2][3] = 0

matriz[3][0] = 0
#Atribui o valor 1 ao elemento na linha 0,coluna 1
matriz[3][1] = 0
#Atribui o valor 0 ao elemento da linha 0, coluna 2
matriz[3][2] = 0
#Atribui o valor 1 ao elemento da linha 0, coluna 3
matriz[3][3] = 0

#exibir os valores da matriz:
#loop esterno para percorrer os indices das linhas (de 0 a 3)
for contador1 in range(4):
   #loop interno para percorrer os indíces das colunas (de 0 a 3)
    for contador2 in range(4):
        #imprime o elemento da matriz na culona atuais, sem adicionar uma nova linha 
        print (matriz[contador1] [contador2], end=" ")
        #imprime uma nova linha após a impressão de todos os elementos de uma linha da matriz
    print()