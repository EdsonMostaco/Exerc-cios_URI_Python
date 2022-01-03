inicio = input()
fim = input()
cont = 0 
        
for ano in range(inicio,fim+1,4):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(ano)
        cont +=1
print('bissextos: {}'.format(cont))
