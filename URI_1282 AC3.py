qtd = int(input())
cont = 0
nomes = []
tInscritos = []
mone = []
cPremium = []
while cont < qtd:
    info = input()
    nome, inscritos, monetizacao, conteudoPremium = info.split(';')
    nome = str(nome)
    inscritos = int(inscritos)
    monetizacao = float(monetizacao)
    conteudoPremium = str(conteudoPremium)
    nomes.append(nome)
    tInscritos.append(inscritos)
    mone.append(monetizacao)
    cPremium.append(conteudoPremium)
    cont +=1
premium = float(input())
nPremium = float(input())
print('-----')
print('BÔNUS')
print('-----')
for i in range(0,qtd):
    if cPremium[i] == 'sim':
        vInscritos = (tInscritos[i]//1000)*premium
        valorFinal = mone[i] + vInscritos
        print('{}:'.format(nomes[i]), 'R$ {:.2f}'.format(valorFinal))
    else:
        vInscritos = (tInscritos[i]//1000)*nPremium
        valorFinal = mone[i] + vInscritos
        print('{}:'.format(nomes[i]), 'R$ {:.2f}'.format(valorFinal))
