tamanhos = int(input())
quantidades = []
for i in range(tamanhos):
    quant = int(input())
    quantidades.append(quant)



pedidos = int(input())
tam = []
for i in range(pedidos):
    tamanho = int(input())



vendidos = 0
for i in range(len(quantidades)):
    for x in range(len(pedidos)):
        if quantidades[x - 1] > 0:
            menos = i - 1
            quantidades.insert(i,menos)
            vendidos += 1
        

#for i in range(0,len(quantidades)):
 # for x in range(0,pedidos):
 #     if i == x:
 #         menos = i - 1
 #         vendidos = vendidos + 1
 #         quantidades.insert(i,menos)

print(vendidos)
