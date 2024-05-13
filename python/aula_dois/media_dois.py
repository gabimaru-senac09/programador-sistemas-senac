# Entrada do usuário
nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite a segunda nota: "))
notas = []

def adicionar_itens(lista, *args):
    lista.extend(args)

adicionar_itens(notas, nota1, nota2)
# notas_a_adicionar = [nota1, nota2]
# notas.extend(notas_a_adicionar)

media = sum(notas) / len(notas)
message = f'A media entre {nota1:.1f} e {nota2:.1f} = {media:.1f}.'

if (media >= 7):
    print(message, "Você está Aprovado")
elif (media < 0):
    print("Digite um valor válido")
else:
    print(message, "Você está reprovado")
 
    


