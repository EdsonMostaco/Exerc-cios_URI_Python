val = input()
x, y = val.split()
x = float(x)
y = float(y)
if x == 0 and y == 0:
    print("Origem")
if x == 0 and y != 0:
    print("Eixo Y")
if x != 0 and y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
    
