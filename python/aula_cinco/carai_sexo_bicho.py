"""
Crie um programa que solicita o sexo do usuário. Caso ele informe F apresente a
mensagem "Sexo Feminino", caso ele informe M, "Sexo masculino". Caso informe alguma
outra opção, "Sexo não definido"
"""
sexo = input("Digite o seu sexo [M - Masculino ou F - Feminino]: ")

match sexo.lower():
    case "m":
        print("Sexo Masculino")
    case "f":
        print("Sexo feminino")
    case _:
        print("Sexo indefinido")