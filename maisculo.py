'''
Podemos utilizar métodos dentro das Strings. Por exemplo, mudar de maisuculo para minusculo.

Lembrando que todo método precisa os parenteses vazios após. Ex: lower()
'''
seq = "ABCDEFGHIJKLMNOP"
seq = seq.lower()
print(seq)

#Exemplo pratico, deixando tudo em minusculo.
a= "Diego"
b= "Mariano"
concatenar = a + " " + b
print(concatenar.lower())

#Exemplo pratico, deixando tudo em maiusculo.
a= "Diego"
b= "Mariano"
concatenar = a + " " + b
print(concatenar.upper())

'''Exemplo pratico, atribuindo upper de forma permanente na variavel. Para isto, é necssario atribiuir o upper na variavel
'''
a= "pamonha"
b= "refri"
concatenar=a+" "+b
concatenar=concatenar.upper()
print(concatenar)

'''
Para adicionar linha automaticamente após aparecer a string, utiliza-se o \n.
'''
a="ouvir musica"
b="é bom demais"
concatenar=a+" "+b+"\n"
print(concatenar)

'''
Da mesma forma, para excluir uma linha, pode-se utilizar o método STRIP, seguido de parenteses: .strip()
A função removeria qualquer espaço “sobrando” no final da frase também

'''
a="ouvir musica"
b="é bom demais"
concatenar=a+" "+b+"\n"
print(concatenar.strip())

'''
.split()
Essa função transforma a variável em listas. Note que o que ventro dentro do parênteses define como será apresentada essa lista.
Se for em branco, a lista virá completa e sem quebras, se colocar a letra r, a lista quebrará sempre que encontrar um r, se colocar um R, virá quebrada quando encontrar um R (lembrando que tem diferença de letras maiúsculas e minúsculas).
'''
minhastring = "o rato roeu a roupa do rei de Roma"
minhalista = minhastring.split()
print(minhalista)

#exemplo tirando a letra r
minhastring = "o rato roeu a roupa do rei de Roma"
minhalista = minhastring.split("r")
print(minhalista)
print('teste')

'''
.find("rei")
Fazer buscas dentro da string, para saber em qual posição se encontra. Lembrando que no parenteses devemos colocar o que estamos buscando.
A resposta será a posição que se encontra a palavra procurada, dentro da string.
'''
minhastring = "o rato roeu a roupa do rei de Roma"
busca = minhastring.find("rei")
print(busca)

'''
Essa busca pode ser útil, se você quer imprimir parcial o texto.
Por exemplo: imprimir “rei de Roma”, dai você descobre qual a posição inicial do Rei (no caso 23) e imprime da posição 23 e diante.
'''
minhastring = "o rato roeu a roupa do rei de Roma"
busca = minhastring.find("rei")
print(minhastring[busca:])

'''
Método Replace: replace (“ “)
substitui uma coisa por outra. Sendo que a primeira definição no parênteses é o que será substituído e a segunda é o que irá substituir / o substituto.
'''
#Para funcionar o REPLACE, é necessário que seja realmente atribuido na string, conforme linha 85.
minhastring = "o rato roeu a roupa do rei de Roma"
minhastring = minhastring.replace("o rei", "a rainha")
print(minhastring)