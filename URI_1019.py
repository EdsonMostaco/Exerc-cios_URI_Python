tempo = int(input())

horas = tempo //(60**2)
tempo = tempo - horas*(60**2)
minutos = tempo //60
segundos = tempo - minutos*60

print (str(horas)+":"+str(minutos)+":"+str(segundos))
    
