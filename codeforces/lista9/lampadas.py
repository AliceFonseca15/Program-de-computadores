botao = int(input())
sequencia = list(map(int,input().split()))

a = 0
b = 0

for i in range(0,len(sequencia)):
    if sequencia[i] == 1:
        if a == 1:
            a = 0
        else: 
            if a == 0:
                a = 1
    if sequencia[i] == 2:
        if a == 1:
            a = 0
        else: 
            if a == 0:
                a = 1
        if b == 1:
            b = 0
        else: 
            if b == 0:
                b = 1
print(a)
print(b)
