def soma(numero):
    separa = list(numero)
    separa_int = [] 
    for i in separa:
        if type(i) == str:
            separa_int.append(int(i))
    s = sum(separa_int)
    
    
    while s >= 10:
        s = sum([int(i) for i in str(s)])
    
    return s

while True:
    valor1, valor2 = input().split()
    if valor1 == '0' and valor2 == '0':
        break

    algarismo1 = soma(valor1)
    algarismo2 = soma(valor2)
    
    if algarismo1 > algarismo2:
        print("1")
    elif algarismo2 > algarismo1:
        print("2")
    else:
        print("0")




