import statistics as avg

lista = [10, 8, 9]
media = avg.mean(lista)


if media >= 7:
    print("Aprovado")
else:
    print("Em recuperação")
    
print(f'A media é igual a {media}')

