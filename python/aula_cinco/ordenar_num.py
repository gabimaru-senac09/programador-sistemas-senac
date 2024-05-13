"""
Faça um programa que leia três números
e mostre-os em ordem crescente.
"""
# numeros = []

# for i in range (1, 4):
#     numero = float(input(f"Digite o {i}° número: "))
#     numeros.append(numero)
numeros = []

numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))
numero_tres = float(input("Digite o terceiro número: "))

if numero_um > numero_dois:
    temp = numero_um
    numero_um = numero_dois
    numero_dois = temp
                     
if numero_dois > numero_tres:
    temp = numero_dois
    numero_dois = numero_tres
    numero_tres = temp

if numero_um > numero_dois:
    temp = numero_um
    numero_um = numero_dois
    numero_dois = temp

print(numero_um, numero_dois, numero_tres)
    
