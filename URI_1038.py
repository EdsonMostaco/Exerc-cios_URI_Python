entrada = input()
codigo, quantidade = entrada.split()
codigo = int(codigo)
quantidade = int(quantidade)

if codigo == 1:
    valor = 4.00
    print("Total: R${:.2f}".format(valor*quantidade))
elif codigo == 2:
    valor = 4.50
    print("Total: R${:.2f}".format(valor*quantidade))
elif codigo == 3:
    valor = 5.00
    print("Total: R${:.2f}".format(valor*quantidade))
elif codigo == 4:
    valor = 2.00
    print("Total: R${:.2f}".format(valor*quantidade))
elif codigo == 5:
    valor = 1.50
    print("Total: R${:.2f}".format(valor*quantidade))
