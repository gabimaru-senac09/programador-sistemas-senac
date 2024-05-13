"""
Faça um programa que solicita um login e senha do usuário e verifique se a 
senha digitada é igual ao login. Caso a senha informada seja igual ao login,
solicite uma nova senha.
"""
login = input("Digite o usuário: ")
senha = input("Digite a senha: ")

while login == senha:
    senha = input("Digite uma nova senha: ")
    print(f"Sua senha é {senha}")
    
    if len(senha) < 8:
        senha = input("Digite uma senha maior: ")
    if len(senha) > 8:
        print(f"Sua senha é {senha}")
        break

        


    
    
    