valores = input()
A,B,C,D = valores.split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if A == C and B == D:
    horas = 24
    print ("O JOGO DUROU %i"%horas,"HORA(S)")
elif A > C:
    horas = (24 - A) + C
    print ("O JOGO DUROU %i"%horas,"HORA(S)", end="")
    if B > C:
        minutos = (59 - B) + D
        print ("E %i"%minutos, "MINUTO(s)")
elif A < C:
    horas = C - A
    print ("O JOGO DUROU %i"%horas,"HORA(S)", end="")
    if B < D:
        minutos = D - B
        print ("E %i"%minutos, "MINUTO(s)")
