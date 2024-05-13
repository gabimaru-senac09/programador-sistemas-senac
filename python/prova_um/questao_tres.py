# Conversor de temperatura
opcao = input("""
Selecione uma das opções 
1 - Converter Celsius para Fahrenheit
2 - Converter Fahrenheit para Celsius 
""")

match opcao:
    case "1":
        temperatura = float(input("Digite a temperatura: "))
        converte_fah = (temperatura * 9/5) + 32 
        print(f"A temperaratura é {converte_fah}F")
        
    case "2":
        temperatura = float(input("Digite a temperatura: "))
        converte_celsius = (temperatura - 32) * 5/9
        print(f"A temperaratura é {converte_celsius}C")
