dia = input("Digite um dia da semana: ")

match dia:
    case "Domingo" | "Sábado":
        print("Final de semana")
    case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta" | "Sábado":
        print("Dia útil")
    case _:
        print(f"{dia} não é um valor válido")