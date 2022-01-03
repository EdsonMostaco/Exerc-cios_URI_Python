tempo = 0
tempos = []
while True:
    tempo = int(input())
    if tempo >= 0:
        tempos.append(tempo)
    else:
        break
media = sum(tempos)/len(tempos)
print('MEDIA: {:.2f}'.format(media))
for i in tempos:
    if i < media:
        print(i)
