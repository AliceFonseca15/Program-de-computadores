lista = []
print("Digite dez números:")
for i in range(10):
    numeros = int(input())
    lista.append(numeros)

positivos = 0
negativos = 0
zeros = 0
for j in range(len(lista)):
    if lista[j] == 0:
        zeros = zeros + 1
    if lista[j] < 0:
        negativos = negativos + 1
    if lista[j] > 0:
        positivos = positivos + 1

print("Postivos:",positivos)
print("Negativos:",negativos)
print("Zeros:",zeros)
print(lista)