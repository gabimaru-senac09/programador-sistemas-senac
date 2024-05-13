        # c1 c2  c3  c = coluna
matriz = [[1, 2, 3],  #linha 0
          [4, 5, 6], # linha 1
          [7, 8, 9]] # linha 2

# print(matriz[0][1])

# matriz[1][0] = 14 # atribuir um novo valor

# Para matrizes quadradas
for i in range(len(matriz)): # Responsável pela posição da linha
    for j in range(len(matriz)): # Responsável pelo posição da coluna
        print(matriz[i][j])


# Para outros tipos de matrizes que não sejam quadradas
matriz_dois = [[1, 2, 3],  
               [4, 5, 6], 
               [7, 8, 9],
               [1, 1, 1]]

# Para o for rodar independente o tamanho da matriz
for i in range(len(matriz_dois)): # Ele vai retornar a quantidade de linhas
    for j in range(len(matriz_dois[0])): # Dessa forma serve você especificar o número de colunas 
        print(matriz_dois[i][j])