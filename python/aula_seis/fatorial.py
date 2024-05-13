# Faça um programa para calcular o fatorial de um número

numero = int(input("Digite um número: "))
fatorial = numero

for i in range(numero -1, 1, -1):
    fatorial *= i
    print(f"{numero} * {i} = {fatorial}")



    

