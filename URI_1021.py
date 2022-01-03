valor = float(input())
valor = valor+0.0001

cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print("NOTAS:")
for cedula in cedulas:
    qtd_cedulas = valor//cedula
    print ("{} nota(s) de R$ {:.2f}".format(qtd_cedulas, cedula))
    valor = valor - qtd_cedulas* cedula
print("MOEDAS:")
for moeda in moedas:
    qtd_moedas = valor//moeda
    print("{} moeda(s) de R$ {:.2f}".format(qtd_moedas, moeda))
    valor = valor - qtd_moedas* moeda

