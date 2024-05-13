"""Altere o programa anterior para que ele informe
a posição do maior elemento (linha e coluna)
do maior"""

matriz = [[0] * 4 for _ in range(4)]
maior = 0
linha_maior = 0
coluna_maior = 0

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = int(input(f"Digite o [{i}][{j}] valor inteiro: "))

        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j

for i in matriz:
    print(i) 

print(f"O maior valor {maior} encontra-se na posição [{linha_maior}][{coluna_maior}]")
    
 