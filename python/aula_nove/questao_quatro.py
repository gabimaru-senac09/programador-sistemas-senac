"""
Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0
os demais elementos. Imprima a matriz no final
"""
matriz = [[0] * 5 for _ in range(5)]

for i in range(5):
    matriz[i][i] = 1
    
for i in matriz:
    print(i)