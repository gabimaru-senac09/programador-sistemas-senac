'''
Programa alistamento militar
'''

sexo = input("Por favor, digite o seu sexo: ")
altura = float(input("Agora digite sua altura em m: "))

if (sexo.lower() == "m" and altura >= 1.70):
    print(f"Sexo: Masculino. Altura = {altura:.2f}m. Apto para o serviço militar")
elif (sexo.lower() == "f" and altura >= 1.60):
    print(f"Sexo: Feminino. Altura = {altura:.2f}m. Apta para o serviço militar")

else:
    if sexo.lower() == "m":
        print("Sexo: Masculino")
    elif sexo.lower() == "f":
        print("Sexo: Feminino")
    print("Não apto para o serviço militar.")
