a = int(input())
b = int(input())
if a < b:
    for i in range(lista[0], lista[1]+1):
        for x in range (1,11):
            print(i, 'x', x, '=', i*x)
        print('----------')
else:
    print('Nenhuma tabuada no intervalo!')
