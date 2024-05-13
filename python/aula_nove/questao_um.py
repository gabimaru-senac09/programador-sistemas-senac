"""
Declare uma matriz para armazenar o nome dos colegas presentes
em aula, com as linhas e colunas conforme a posição dos mesmos.
Ao final, imprima os elementos.

Coleguinhas:
Felipe, Luiz Felipe, Adriel, Pedro,
Higor, Gil, Maynara, Adrian, Luiz Carlos,
Luiz Gustavo, Gabriel, Arthur, Anderson
"""
coleguinhas = [["Felipe", "Luiz Felipe", "", "Adriel"],
               ["Pedro", "Higor", "Gil", "Maynara"],
               ["", "Adrian", "Luiz Carlos", "Luiz Gustavo"],
               ["", "Gabriel", "", "Arthur"],
               ["", "", "Anderson", ""]]

for i in range(len(coleguinhas)):
    for j in range(len(coleguinhas[0])):
        print(coleguinhas[i][j])
    print("-----------")
