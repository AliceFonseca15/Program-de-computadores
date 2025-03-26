tamanhos = int(input())
quantidades = []
for i in range(tamanhos):
    quant = int(input())
    quantidades.append(quant)


pedidos = int(input())
tam = []
for i in range(pedidos):
    tamanho = int(input())
    tam.append(tamanho)


vendidos = 0
for i in range(len(tam)):
    for j in range(len(quantidades)):
        indice = tam[i] - 1
        if j == indice:
            if tam[i] != 0:
                quantidades[j] = quantidades[j] - 1
                if quantidades[j] < 0:
                    quantidades[j] = 0
                else:
                    vendidos = vendidos + 1

print(vendidos)

