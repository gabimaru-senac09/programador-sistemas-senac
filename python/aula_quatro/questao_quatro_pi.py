# # Faça um programa que leia três números e mostre o maior deles
numeros = []

for i in range(1, 4, 1):
    numero = float(input("Digite um numero: "))
    numeros.append(numero)

if numeros[0] > numeros[1] and numeros[0] > numeros[2]:
    print(f"{numeros[0]} é maior que {numeros[1]} e {numeros[2]}")
elif numeros[1] > numeros[0] and numeros[1] > numeros[2]:
    print(f"{numeros[1]} é maior que {numeros[0]} e {numeros[2]}")
else:
    print(f"{numeros[2]} é maior que {numeros[0]} e {numeros[1]}")
