gastos = {'pessoal':0, 'trabalho':0, 'outros':0, 'lazer':0}

continuar = True
while continuar == True:
    valor_do_gasto = float(input('Informe um valor:'))
    categoria = input('Informe uma categoria:').lower()
    #Verifica se a categoria ja existe no dicionario
    if categoria in gastos.keys():
        #categoria ja existe
        gastos[categoria] += valor_do_gasto
    else:
        gastos['outros'] += valor_do_gasto
    print(gastos)
    continuar = input('Continuar?').lower() == 's'

#Passa por todas as categorias e exibe os gastos
for categoria in gastos.keys():
    print('Categoria:', categoria, 'Valor:', gastos[categoria])
    
