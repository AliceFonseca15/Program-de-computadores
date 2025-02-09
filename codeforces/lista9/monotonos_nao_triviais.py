valor = int(input()) 
letras = input()  
lista_letras = list(letras)  


nova = []
for i in lista_letras:
    if i == 'a':  
        nova.append(1)
    else:
        nova.append(2)

contagem = 0
for i in range(1, len(nova)):
    if nova[i] == 1 and nova[i] == nova[i - 1] and nova[i - 3] == 2:
        contagem += 2
    else:
        if nova[i] == 1 and nova[i] == nova[i - 1]:  
            contagem += 1
        


print(contagem)