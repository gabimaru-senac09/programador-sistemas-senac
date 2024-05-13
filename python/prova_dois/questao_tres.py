"""
Faça um programa que leia dois vetores de 5 elementos.
Crie um vetor que seja a intersecção entre 2 vetores anteriores, ou seja,
que contém apenas os números que estão em ambos os vetores. Não deve
conter números repetidos.
"""
vetor_um = []
vetor_dois = []
interseccao = []

for i in range(5):
    valor = int(input(f"Digite {i+1} valor do vetor_um: "))
    vetor_um.append(valor)
    
for i in range(5):
    valor = int(input(f"Digite {i+1} valor do vetor_dois: "))
    vetor_dois.append(valor)
    
for i in vetor_um:
    if i in vetor_dois and i not in interseccao:
        interseccao.append(i)
        

            
print(vetor_um)
print(vetor_dois)
print(interseccao)