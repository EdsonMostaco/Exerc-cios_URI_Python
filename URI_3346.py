F1,F2 = input().split()
F1 = float(F1)
F2 = float(F2)
F_final = ((1+(F1/100))*(1+(F2/100)))
print('{:.6f}'.format(F_final))