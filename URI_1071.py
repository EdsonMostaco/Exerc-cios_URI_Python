x = int(input())
y = int(input())

maior = x if x > y else y
menor = y if y < x else x
menor += 1
soma = 0

for n in range(menor, maior):
    if n % 2 != 0:
        soma += n
print (soma)
