vetor_nomes = ["Mayara", "Luiz Carlos", "Luiz Gustavo"]

# Imprimir uma posição no vetor
#print(vetor_nomes[1]) # Imprime "Luiz Carlos"

# Alterar a posição do vetor
vetor_nomes[0] = "João"

# Adicionar um elemento ao final da lista
vetor_nomes.append("Gabriel")

# Inserir um elemento em uma posição específica
vetor_nomes.insert(5, "Gabriel")

# Remover o último elementto da lista
vetor_nomes.remove("Gabriel")

# Remover um elemento de uma posição específica
#valor_removido = vetor_nomes.pop(7)

# Contar o número de vezes que o elemento aparece
ocorrencias = vetor_nomes.count("Luiz Carlos")

# Percorrer todos os elementos na lista
# for i in vetor_nomes:
#     print(i)

print(ocorrencias)

# Mostrar a quantidade de elementos da lista
print(f"O vetor nomes possui {len(vetor_nomes)} nomes")

