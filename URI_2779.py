n = int(input())
m = int(input())
cont = 0
lista = []
while m > cont:
    x = int(input())
    lista.append(x)
    cont +=1
figurinhas = set(lista)
print('{}'.format(n-len(figurinhas)))
    
