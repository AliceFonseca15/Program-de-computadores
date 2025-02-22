sequencia = (input())

a = 0
c = 0
g = 0
t = 0

sec = list(map(str, sequencia)) 

for i in sequencia:
    if i == "A" or i == "a":
        a = a + 1
    if i == "C" or i == "c":
        c = c + 1
    if i == "G" or i == "g" :
        g = g + 1
    if i == "T" or i == "t":
        t = t + 1

numero = [a,c,g,t]
print(max(numero))
