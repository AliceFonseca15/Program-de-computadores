minuto, amplitude = map(int,input().split())
valores = list(map(int, input().split()))

valores.sort() 
resultado = []
indice = 0

for i in range(1, amplitude + 1):
    while indice < minuto and valores[indice] < i:
        indice += 1
    resultado.append(minuto - indice)
print(*resultado)
