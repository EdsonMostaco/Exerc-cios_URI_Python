quantidade = int(input())
cont = 0
x = []
while cont < quantidade:
    n = input()
    a,b,c = n.split()
    a = float(a)
    b = float(b)
    c = float(c)
    media = ((a*2)+(b*3)+(c*5))/10
    x.append(media)
    cont +=1
for y in range (0, quantidade):
    print('%.1f'%x[y])
