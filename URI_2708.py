jipe = 'SALIDA'
cont = 0
lista = 0
while jipe == 'SALIDA' or jipe == 'VUELTA':
    info = input()
    if info == 'ABEND':
        break
    else:
        jipe,passageiro = info.split()
        jipe = str(jipe)
        passageiro = int(passageiro)
    if jipe == 'SALIDA':
        lista = lista + passageiro
        cont +=1
    elif jipe == 'VUELTA':
        lista = lista - passageiro
        cont -=1    
print('{}'.format(lista))
print('{}'.format(cont))
