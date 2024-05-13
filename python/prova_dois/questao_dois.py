"""
Faça um programa que leia um vetor de 10 posições e o compacte, ou seja,
elimina as posições com valor zero. Para isso, todos os elementos
a frente do valor zero, devem ser movidos uma posição atrás no vetor
"""
vetor = []

for i in range(10):
    valor = int(input(f"Digite o {i+1}° valor: "))
    vetor.append(valor)


vetor_compactado = []
for valor in vetor:
    if valor != 0:
        vetor_compactado.append(valor)


print(vetor_compactado)
