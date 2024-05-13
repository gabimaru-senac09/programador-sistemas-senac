# # Faça um programa que leia três números e mostre o maior deles
# a = float(input("Digite o 1 primeiro número: "))
# b = float(input("Digite o 2 primeiro número: "))
# c = float(input("Digite o 3 primeiro número: "))

# map percorre uma lista de métodos e executa cada um deles. split vai dividir os inputs por um delimitador.
a, b, c = map(float, input("Digite três valores na mesma linha: ").split())

if (a > b and a > c):
    print(f"{a} é maior que {b} e {c}")
elif (b > c and b > a):
    print(f"{b} é maior que {a} e {c}")
else:
    print(f"{c} é maior que {a} e {b}")