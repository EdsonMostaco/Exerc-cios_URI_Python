x = 0
idade = 0
cont = 0
while x >= 0:
    x = int(input())
    if x >= 0:
        idade = idade + x
        cont += 1
media = (idade/cont)
print ('{:.2f}'.format(media))
    
    
