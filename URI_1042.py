x = input().split()
a, b, c = x
a = int(a)
b = int(b)
c = int(c)

lista = [a,b,c]
lista_nova = sorted(lista)

print("%i"%lista_nova[0],"\n","%i"%lista_nova[1],"\n","%i"%lista_nova[2])
print("\n","%i"%lista[0],"\n","%i"%lista[1],"\n","%i"%lista[2])
