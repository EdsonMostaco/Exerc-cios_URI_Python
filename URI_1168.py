a = int(input())
b = int(input())
x=0
y=0
cont = 0
for y in range(a, b+1):
    for i in range (2, y):
        resto = (y % i)
        if y!=i and y!=1 and resto!=0:
            x +=resto
        else:
            x=0
            break
    if x > 0 or y==2:
        print(y)
        y+=1
        cont +=1
print('primos: {}'.format(cont))
