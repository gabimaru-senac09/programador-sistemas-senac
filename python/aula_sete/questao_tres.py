"""
Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 2 caracteres
b. Idade: entre 0 e 120 
c. Salário: maior que 0
d. Sexo: F ou M
e. Estado civil: s c v d
"""

nome = input("Digite um nome: ")

while len(nome) <= 2:
    nome = input("Digite um nome maior que 2 caracteres: ")

idade = int(input("Digite a idade: "))

while True:
    if idade > 0 and idade <= 120:
        break
    else:
        idade = int(input("Digite uma idade válida: "))

salario = float(input("Digite um salário: R$"))

while salario < 0:
    salario = float(input("Digite um salário válido. R$"))
    
sexo = input("Digite o sexo: ")

while sexo.lower() != "m" and sexo.lower() != "f":
    sexo = input("Digite um sexo válido: [m-f] ")
    
estado_civil = input("Digite o estado civil [s c v d]: ")

while True:
    if estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
        estado_civil = input("Digite um estado civil válido: ")
    else:
        break

print(f"""
Nome: {nome}
Idade: {idade}
Salário: {salario}
Sexo: {sexo}
Estado Civil: {estado_civil}
      """)
