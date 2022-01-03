dia_semana = str(input())
qtd_dias = int(input())

if dia_semana == "domingo":
    dia_semana = 0
elif dia_semana == "segunda":
    dia_semana = 1
elif dia_semana == "terca":
    dia_semana = 2
elif dia_semana == "quarta":
    dia_semana = 3
elif dia_semana == "quinta":
    dia_semana = 4
elif dia_semana == "sexta":
    dia_semana = 5
elif dia_semana == "sabado":
    dia_semana = 6

if qtd_dias == 0:
    print ("chega hoje!")
else:
    if dia_semana == 0:
        dia_semana = dia_semana + qtd_dias
    elif qtd_dias == 7:
        dia_semana == dia_semana
    elif qtd_dias + dia_semana <= 6:
        dia_semana = qtd_dias + dia_semana
    else:
        dia_semana = (qtd_dias + dia_semana)-7
    if dia_semana == 0:
        dia_semana = "domingo"
    elif dia_semana == 1:
        dia_semana = "segunda"
    elif dia_semana == 2:
        dia_semana = "terca"
    elif dia_semana == 3:
        dia_semana = "quarta"
    elif dia_semana == 4:
        dia_semana = "quinta"
    elif dia_semana == 5:
        dia_semana = "sexta"
    elif dia_semana == 6:
        dia_semana = "sabado"
    print ("sera entregue " + str(dia_semana))
    


    
