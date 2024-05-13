import time
"""
Suponha que você está desenvolvendo o sistema de um hotel
que deve abrir um menu de opções para o cliente, as opções dele, são:
1. Fazer Check-in
2. Chamar serviço de quarto
3. Fazer pedido
4. Fazer check-out
"""

while True:
    message_one = "Bem-vindo ao Hotel Casarão. Onde seus sonhos viram realidade!"
    art = open('xerosa.txt', 'r')
    message_two = """
    Digite uma das opções:
1 - Fazer check-in
2 - Chamar serviço de quarto
3 - Fazer pedido
4 - Fazer check-out
5 - Sair
"""

    print(message_one)
    print(art.read())
    time.sleep(2)
    art.close()
    
    opcao = input(message_two)

    match opcao:
        case '1':
            print("Bora fazer o checkin e iniciar os trabalhos")
        case '2':
            print("O serviço de quarto vai ter atender jajá jovem!")
        case '3':
            print("Bora fazer um pedido e tomar uns drinks")
        case '4':
            print("Já vai? Volte sempre e não se esqueça de recomendar a gente!")
        case '5':
            print("Nos chame quando precisar de algo!")
            break
        case _:
            print("Digite uma opção válida!")
            