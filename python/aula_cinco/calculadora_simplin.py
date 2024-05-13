"""
Faça um programa que peça ao usuário dois números.
Depois solicite a ele qual operação aritmética deseja realizar
(soma +, subtração, - , multiplicação *, divisão /). No fim,
imprima o resultado da operação solicitada.
"""

numero_um = float(input("Digite o 1° número: "))
numero_dois = float(input("Digite o 2° número: "))

operacao = input("Digite a operação [soma +, subtração, - , multiplicação *, divisão /]: ")

match operacao:
    case '+':
        resultado = numero_um + numero_dois
        print(f"A soma entre {numero_um} + {numero_dois} = {resultado}")
    case '-':
        resultado = numero_um - numero_dois
        print(f"A subtração entre {numero_um - numero_dois}")
    case '*':
        resultado = numero_um * numero_dois
        print(f"A subtração entre {numero_um} * {numero_dois} = {resultado}")
    case '/':
        resultado = numero_um / numero_dois
        print(f"A subtração entre {numero_um} / {numero_dois} = {resultado}")