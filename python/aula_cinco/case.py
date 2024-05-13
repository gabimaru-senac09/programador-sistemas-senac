dia = input("""Digite um dia da semana: 
1 - Domingo
2 - Segunda
3 - Terça
4 - Quarta
5 - Quinta
6 - Sexta
7 - Sábado
""")

match dia:
    case '1':
        print("Domingo")
    case '2':
        print("Segunda")
    case '3':
        print("Terça")
    case '4':
        print("Quarta")
    case '5':
        print("Quinta")
    case '6':
        print("Sexta")
    case '7':
        print("Sabado")
    case _:
        print("Digite um valor válido")