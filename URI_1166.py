divida = int(input())
pagamento = int(input())
if pagamento >= divida:
    cont = 1
    print('pagamento: {}'.format(cont))
    print('antes = {}'.format(divida))
    print('depois = {}'.format(divida-divida))
    print('-----')
parcela = divida//pagamento
if divida%pagamento != 0:
    parcela +=1
    sobra = divida%pagamento
cont = 1
while cont < parcela:
    while divida > pagamento:
        print('pagamento: {}'.format(cont))
        antes = divida
        divida = divida-pagamento    
        depois = divida
        parcela -= 1
        cont += 1
        
        print('antes = {}'.format(antes))
        print('depois = {}'.format(depois))
        print('-----')
    divida = sobra
    pagamento = sobra
    print('pagamento: {}'.format(cont))
    antes = divida
    divida = divida-pagamento    
    depois = divida
    cont -= 1
        
    print('antes = {}'.format(antes))
    print('depois = {}'.format(depois))
    print('-----')
