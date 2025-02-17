pedidos = [1,3]
quantidades = [4,2,0,3,2]

vendidos = 0
for i in range(len(pedidos)):
    if quantidades[i - 1] >= 0:
        valor = quantidades[i - 1]
        novo = valor - 1
        quantidades.insert(quantidades[i - 1],novo)
        vendidos += 1
    else:
        if quantidades[i - 1] == 0:
            valor =  quantidades[0]
            v = valor - 1
            quantidades.insert(quantidades[i - 1],v)

print("vendidos:",vendidos)
print("quantidades",quantidades)