"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10.
O usuário deve informar de qual número ele deseja ver a tabuada. 
A saída deve ser conforme o exemplo:
"""

i = 1
numero = int(input("Digite um número: "))

while i <= 10:
    print(f"{numero} * {i} = {numero * i}")
    i += 1
