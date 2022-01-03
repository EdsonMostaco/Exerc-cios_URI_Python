valor_produto = float(input())
qtd_produto = int(input())

desconto = 10/100
desconto_adicional = qtd_produto/100

valor_compra = valor_produto * qtd_produto
valor_desconto = valor_compra - ((valor_compra * desconto)+(valor_compra * desconto_adicional))

print ("%.2f"%valor_compra)
print ("%.2f"%valor_desconto)
