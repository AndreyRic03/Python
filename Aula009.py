''' atribuição de uma string dentro de uma variável '''
frase = 'Curso em Vídeo Python'

''' o string atribui para cada algarismo um microespaço dentro da memória do seu computador começando pelo 0 '''

''' fatiamento de valores dentro de uma string '''
print (frase[9])
''' pega o algarismo que está na posição 9 '''

''' pega todas as letras do "9" até o "14" mas excluindo o 14 '''
print (frase[9:14])

''' pega do 9 até 0 21 mas excluindo  21 '''
print (frase[9:21])

''' pega do 9 até o 21 mas pulando de 2 em 2 '''
print (frase[9:21:2])

''' pega todos os valores até o cinco mas excluindo ele '''
print (frase[:5])

''' vai do 15 até o final '''
print (frase[15:])

''' vai do 9 até o final pulando de 3 em 3 '''
print (frase[9::3])


''' vê quantos caracteres tem a frase '''
len(frase)

''' vê quantas letras "O" tem na frase '''
frase.count('o')
''' Outro comando com count, lê quantas letras "o" tem do 0 ao 13 mas excluindo ele. '''
frase.count('o', 0, 13)


''' vê qual caracter começa a palavra '''
frase.find('deo')

''' Se existe a palavra na variavel '''
'Curso' in frase