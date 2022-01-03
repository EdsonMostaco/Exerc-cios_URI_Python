x = int(input())
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z']
for v in range (1,x+1):
    print(str(alfabeto[v-1]*v))
