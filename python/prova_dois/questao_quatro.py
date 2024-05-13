"""
Faça um programa que preenche uma matriz com o produto do valor
da linha e da coluna de cada elemento. Em seguida, imprima na tela
a matriz
"""
matriz = [[0] * 3 for _ in range(3)]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        matriz[linha][coluna] = linha * coluna

for i in matriz:
    print(i)
        