N = int(input())
cont = 0
listaDentro = []
listaFora = []
while cont < N:
    x = int(input())
    if x >=10 and x <= 20:
        listaDentro.append(x)
        cont +=1
    else:
        listaFora.append(x)
        cont +=1
print('{}'.format(len(listaDentro)),'in')
print('{}'.format(len(listaFora)),'out')
