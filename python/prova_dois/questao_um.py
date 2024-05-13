"""
Faça um programa para ler 5 valores e, em seguida, mostre a posição
onde se encontram o maior e o menor valor
"""

matriz = [[0] * 3 for _ in range(3)]
maior = 0
menor = float('inf') # Utilizando o infinito positivo

linha_maior = 0
coluna_maior = 0

linha_menor = 0
coluna_menor = 0

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = int(input(f"Digite o valor para posição [{i}][{j}]: "))
        
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j
        
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            linha_menor = i
            coluna_menor = j 
    
print(f"O número {maior} é o maior número e encontra-se na posição [{linha_maior}][{coluna_maior}]")
print(f"O número {menor} é o menor número e encontra-se na posição [{linha_menor}][{coluna_menor}]")
