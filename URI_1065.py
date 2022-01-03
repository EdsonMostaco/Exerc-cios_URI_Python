valores = []
for i in range(5):
    val = int(input())
    valores.append(int(val))
pares = 0
for j in range(5):
    if valores[j]%2 == 0:
        pares += 1
print (pares, "valores pares")
    
