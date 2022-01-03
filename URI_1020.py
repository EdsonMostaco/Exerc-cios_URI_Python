tempo = int(input())

ano = tempo //365
tempo = tempo - ano*365
meses = tempo // 30
dias = tempo - meses*30

print(ano, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")
