"""Leia uma matriz 4 x 4, conte e escreva
quantos valores maiores que 10 ela possui"""

matriz = [[0] * 4 for _ in range(4)]
count = 0

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = int(input(f"Digite o [{i}][{j}] valor inteiro: "))

        if matriz[i][j] > 10:
            count += 1

for i in matriz:
    print(i) 

print(f"{count} valores maiores que dez")
    
 