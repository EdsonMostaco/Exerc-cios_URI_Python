valores = input()
a,b = valores.split()
a = int(a)
b = int(b)

if a == b:
    horas = 24
    print ("O JOGO DUROU %i"%horas,"HORA(S)")
elif a > b:
    horas = (24 - a) + b
    print ("O JOGO DUROU %i"%horas,"HORA(S)")
elif a < b:
    horas = b - a
    print ("O JOGO DUROU %i"%horas,"HORA(S)")
