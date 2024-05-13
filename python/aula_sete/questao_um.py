"""
Faça um programa que peça duas notas,
entre 0 e 10. Mostre uma mensagem caso o valor inserido
seja inválido
"""
media = 0

while media < 7:
    nota_um = float(input("Digite a primeira nota: "))
    nota_dois= float(input("Digite a segunda nota: "))
    media = (nota_um + nota_dois)/2
    
    print(media)
    
    if media >= 7:
        print("Parábens, você passou")
        break
    else: 
        print("O miserável não é gênio. Digite uma nota válida")
    

