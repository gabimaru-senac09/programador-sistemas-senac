coleguinhas_queridos = ["Maynara", "Luiz Carlos", "Luiz Gustavo", "Arthur", "Anderson", "Gabriel", "Luana", "Adrian", "Higor", "Pedro"]

# for i in coleguinhas_queridos:
#     print(i)
    
# for i in range (0, len(coleguinhas_queridos)):
#     print(coleguinhas_queridos[i])

# Altere o programa anterior e insira o colega que chegou atrasado
# coleguinhas_queridos.append("Adrian")
count = 0

# Busque nesse vetor de nomes, a quantidade de nomes que iniciam em "A"
for i in coleguinhas_queridos:
    if i.startswith("A"):
        count += 1

print(count)
        
# Outra forma
for i in coleguinhas_queridos:
    # i eu percorro cada elemento da lista, as chaves percorre o index dentro do elemento
    if i[0] == "A" or i[0] == "a":
        count += 1

print(f"A quantidade de coleguinhas com a como letra inicial é {count}")
