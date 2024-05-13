"""
Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores
de cada posição das matrizes lidas
"""
matriz_um = [[0] * 4 for _ in range(4)]
matriz_dois = [[0] * 4 for _ in range(4)]
maiores_valores = [[0] * 4 for _ in range(4)]

for i in range(len(matriz_um)):
    for j in range(len(matriz_um[0])):
        matriz_um[i][j] = int(input(f"Digite o valor da posição [{i}][{j}]: "))

for i in range(len(matriz_dois)):
    for j in range(len(matriz_dois[0])):
        matriz_dois[i][j] = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        
for i in range(len(maiores_valores)):
    for j in range(len(maiores_valores[0])):
        if matriz_um[i][j] > matriz_dois[i][j]:
            maiores_valores[i][j] = matriz_um[i][j]
        else:
            maiores_valores[i][j] = matriz_dois[i][j]

for i in matriz_um:
    print(i)
print("----------")

for i in matriz_dois:
    print(i)
print("----------")

for i in maiores_valores:
    print(i)
print("----------")