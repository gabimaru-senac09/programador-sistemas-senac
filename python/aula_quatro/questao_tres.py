"""
Faça um programa que verifique se o sexo do usuário é F-Feminino
 e M-Masculino. Confirme e escreva o sexo digitado pelo usuário
""" 

sexo = input("Digite o sexo do usuário: ")

if sexo.lower() == "masculino" or sexo.lower() == "m":
    print("A cria é masculina.")
elif sexo.lower() == "feminino" or sexo.lower() == "f":
    print("A cria é feminina.")
else:
    print("Valor indefinido")
