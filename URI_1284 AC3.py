qtd = int(input())
cont = 0
nOrigem = []
nAtivi = []
nAlt = 0
while cont < qtd:
    nota = float(input())
    nOrigem.append(nota)
    cont +=1
while cont > 0:
    nota = float(input())
    nAtivi.append(nota)
    cont -=1
for i in range(0,qtd):
    if nOrigem[i] < 10 and nAtivi[i] == 10.00:
        nAlt +=1
print('NOTAS ALTERADAS: {}'.format(nAlt))
for i in range(0,qtd):
    if nOrigem[i] == 10.00:
        print('-({:03d})'.format(i+1),'original: %05.2f'%nOrigem[i], '| final: %05.2f'%nOrigem[i])
    elif nAtivi[i] == 10.00:
        if nOrigem[i] + 2 > 10:
            nNota = 10
            print('*({:03d})'.format(i+1),'original: %05.2f'%nOrigem[i], '| final: %05.2f'%nNota)
        else:
            nNota = nOrigem[i] + 2
            print('*({:03d})'.format(i+1),'original: %05.2f'%nOrigem[i], '| final: %05.2f'%nNota)     
    else:
        nNota = nOrigem[i]
        print('-({:03d})'.format(i+1),'original: %05.2f'%nOrigem[i], '| final: %05.2f'%nOrigem[i])
