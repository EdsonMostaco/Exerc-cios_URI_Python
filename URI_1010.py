A1_B1_C1 = input()
A1, B1, C1 = A1_B1_C1.split()
A1 = int(A1)
B1 = int(B1)
C1 = float(C1)

A2_B2_C2 = input()
A2, B2, C2 = A2_B2_C2.split()
A2 = int(A2)
B2 = int(B2)
C2 = float(C2)

pagar = (B1*C1)+(B2*C2)

print ("VALOR A PAGAR: R$ %.2f"%pagar)
