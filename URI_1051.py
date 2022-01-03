renda = float(input())
if renda <= 2000.00:
    print('Isento')
elif renda > 2000.00 and renda <= 3000.00:
    renda = renda - 2000
    imposto = renda * (8/100) - 100
    print('R$ {:.2f}'.format(imposto))
elif renda > 3000.00 and renda <= 4500.00:
    renda = renda - 2000
    imposto = renda * (18/100) - 100
    print('R$ {:.2f}'.format(imposto))
else:
    imposto = renda * (28/100) - 100
    renda = renda - 2000
    print('R$ {:.2f}'.format(imposto))
