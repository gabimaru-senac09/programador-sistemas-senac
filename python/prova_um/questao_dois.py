"""
Escreva um programa que leia três números do usuário e imprima
o maior e o menor desses números
"""
numero_um = float(input("Digite o 1° número: "))
numero_dois = float(input("Digite o 2° número: "))
numero_tres = float(input("Digite o 3° número: "))

# Maior número
if numero_um > numero_dois and numero_um > numero_tres:
    print(f"{numero_um} é maior que {numero_dois} e {numero_tres}")
elif numero_dois > numero_um and numero_dois > numero_tres:
    print(f"{numero_dois} é maior que {numero_um} e {numero_tres}")
else:
    print(f"{numero_tres} é maior que {numero_um} e {numero_dois}")
    
# Menor número
if numero_um < numero_dois and numero_um < numero_tres:
    print(f"{numero_um} é menor que {numero_dois} e {numero_tres}")
elif numero_dois < numero_um and numero_dois < numero_tres:
    print(f"{numero_dois} é menor que {numero_um} e {numero_tres}")
else:
    print(f"{numero_tres} é menor que {numero_um} e {numero_dois}")




