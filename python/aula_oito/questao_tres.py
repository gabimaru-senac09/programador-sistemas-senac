# Faça um programa que leia um vetor de 5 números
# e mostre-os na ordem inversa

vetor = [4, 3, 5, 10, 1]
# reverse = vetor.reverse()

# for i in vetor:
#     print(i)

ordem_descre = sorted(vetor)

#   Outra forma se for descrente. 
for i in range(len(vetor) - 1, -1, -1):
     print(ordem_descre[i])
    
