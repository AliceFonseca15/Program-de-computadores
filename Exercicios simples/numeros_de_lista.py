lista1 = list(map(int,input().split()))
lista2 = list(map(int,input().split()))
lista_não_presentes = []
for i in range(len(lista2)):
    if lista2[i] not in lista1:
        lista_não_presentes.append(lista2[i])
print(*lista_não_presentes)
