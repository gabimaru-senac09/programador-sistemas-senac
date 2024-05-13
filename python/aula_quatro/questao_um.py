# Faça um programa que peça dois números e imprima o maior deles
numero1 = float(input("Digite o 1 numero: "))
numero2 = float(input("Digite o 2 numero: "))

if (numero1 > numero2 and numero2 < numero1):
    print(f"{numero1} é maior que {numero2}")
elif (numero1 == numero2):
	print(f"{numero1} e {numero2} são iguais")
else:
    print(f"{numero2} é maior que {numero1}")
