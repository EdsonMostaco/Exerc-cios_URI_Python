x = int(input())
if x > 5 and x < 2000:
    for n in range (1,x+1):
        if n % 2 == 0:
            par = n
            quadrado = n**2
            print(f"{n}^2 = {quadrado}")
