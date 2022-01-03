doacao = 0
vicCoin = 2.50
novaDoacao = 0
while novaDoacao >= 0:
    novaDoacao = float(input())
    if novaDoacao >=0:
        doacao = doacao + novaDoacao
    else:
        break

VCS = doacao
valor = VCS*vicCoin

print('VC$ {:.2f}'.format(VCS))
print('R$ {:.2f}'.format(valor))
