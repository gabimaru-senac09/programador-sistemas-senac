def contas(centros):
    match centros:
        case [area, centros]: # Apenas 1 centro de custo
            print("A área {} possui o centro de custo {}".format(area,centros))

        case [area, *centros]: #2 ou mais centros
            print('A área {} possui os centros de custo abaixo:'.format(area))
            for centro in centros:
                print (centro)
                
contas(['Financeiro', 'ABC'])
contas(['Marketing', 'ABC','XYZ','HJG'])
