#Letra I
#programa que imprime os dez primeiros numeros da serie de fibonnacci com while
primeiro = 1
segundo = 1
print(primeiro)
print(segundo)
cont = 2
while cont < 15:
    proximo = primeiro + segundo
    print(proximo)
    primeiro = segundo
    segundo = proximo
    cont += 1
print("fim da serie fibonnacci")