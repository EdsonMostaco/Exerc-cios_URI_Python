n = 0
arq = []
cont = 0
while cont < 100:
    n = int(input())
    arq.append(n)
    cont += 1
maior = max(arq)
posicao = arq.index(maior)
print(maior)
print(posicao+1)
