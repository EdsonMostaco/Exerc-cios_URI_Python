N = float(input())


total = N

notaDeCem = 0
notaDeCinquenta = 0
notaDeVinte = 0
notaDeDez = 0
notaDeCinco = 0
notaDeDois = 0

moedaDeUm = 0
moedaDe50 = 0
moedaDe25 = 0
moedaDe10 = 0
moedaDe05 = 0
moedaDe01 = 0

while total >= 100.00:
    total = total - 100.00
    notaDeCem += 1

while total >= 50.00:
    total = total - 50.00
    notaDeCinquenta += 1

while total >= 20.00:
    total = total - 20.00
    notaDeVinte += 1

while total >= 10.00:
    total = total - 10.00
    notaDeDez += 1

while total >= 5.00:
    total = total - 5.00
    notaDeCinco += 1

while total >= 2.00:
    total = total - 2.00
    notaDeDois += 1

while total >= 1.00:
    total = total - 1.00
    moedaDeUm += 1

while total >= 0.50:
    total = total - 0.50
    moedaDe50 += 1

while total >= 0.25:
    total = total - 0.25
    moedaDe25 += 1

while total >= 0.10:
    total = total - 0.10
    moedaDe10 += 1

while total >= 0.05:
    total = total - 0.05
    moedaDe05 += 1

while total >= 0.01:
    total = total - 0.01
    moedaDe01 += 1

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(notaDeCem))
print("{} nota(s) de R$ 50.00".format(notaDeCinquenta))
print("{} nota(s) de R$ 20.00".format(notaDeVinte))
print("{} nota(s) de R$ 10.00".format(notaDeDez))
print("{} nota(s) de R$ 5.00".format(notaDeCinco))
print("{} nota(s) de R$ 2.00".format(notaDeDois))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(moedaDeUm))
print("{} moeda(s) de R$ 0.50".format(moedaDe50))
print("{} moeda(s) de R$ 0.25".format(moedaDe25))
print("{} moeda(s) de R$ 0.10".format(moedaDe10))
print("{} moeda(s) de R$ 0.05".format(moedaDe05))
print("{} moeda(s) de R$ 0.01".format(moedaDe01))
