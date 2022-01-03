a = input()
lista = []
lista.append(a.split())
cmd = ''
x = ''
while x != 'encerrar':
    x = input()
    if x == 'encerrar':
        break
    elif x == 'exibir':
        for i in sorted(lista):
            if i < len(lista)-1:
                print(i,end='')
            else:
                print()
    else:
        cmd,valor = x.split()
        if cmd == 'adicionar':
            lista.append(valor)
        elif cmd == 'remover':
            try:
                lista.remove(valor)
            except:
                print('código {} não encontrado'.format(valor))
    
