notas = input()
n1,n2,n3,n4 = notas.split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1*2)+(n2*3)+(n3*4)+n4)/10
print ("Media: %.1f" %media)
if media >= 7.0:
    print ("Aluno aprovado.")
elif media >= 5.0 and media < 7:
    print ("Aluno em exame.")
    n_exame = float(input())
    media_final = (media + n_exame)/2
    print ("Nota do exame: %.1f" %n_exame)
    if media_final >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f" %media_final)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f" %media_final)
else:
    print("Aluno reprovado.")
