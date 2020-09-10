#Lista vazia com as temperaturas
#temperaturas = [23, 5, -6, 34]
temperaturas = []


print(temperaturas)


#Pede para o usuario digitar 5 temperaturas
contador = 0
while contador < 5:
  temperatura = float(input('Informe uma temperatura:'))
  #Adiciona temperatura no final
  temperaturas.append(temperatura)
  print(temperaturas)
  contador += 1

#Encontrar o maior valor
maior = max(temperaturas)
print('Maior valor:', maior)

#Encontra o valor menor
menor = min(temperaturas)
print('Menor valor:', menor)
