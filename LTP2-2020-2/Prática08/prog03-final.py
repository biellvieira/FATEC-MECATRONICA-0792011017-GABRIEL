personagens = {'dps': [] , 'helaer': [] , 'support': [] , 'tank': [] }

continuar = True

quantidade_de_personagens = int(input('Informe a quantidade de personagens:'))
contador = 0

while contador < quantidade_de_personagens:
    classe = input('Informe a classe:').lower()
    nome = input('Informe o nome:')
    if classe in personagens.keys():
        personagens[classe].append(nome)
        contador += 1
    else:
        print('Classe de personagem invalida!')
    print(personagens)

print('Porcentagens relativas:')
for categoria in personagens.keys():
    porcentagem = len(personagens[categoria])/quantidade_de_personagens
    print('Categoria:' , categoria, ' - ', porcentagem * 100)

print('Personagens:')
for categoria in personagens.keys():
    print('Classe de personagem:',  categoria.capitalize())
    for nome_de_personagem in personagens[categoria]:
        print(nome_de_personagem)
    print('--------')        
