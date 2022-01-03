trabalho = float(input())
prova = float(input())

media_final = (trabalho * 0.5)+(prova * 0.5)

if trabalho < 2:
    print("reprovado")
elif media_final < 6 and media_final >=1:
    print("talvez com a sub")
elif media_final >= 6:
    print("aprovado")
else:
    print("reprovado")
