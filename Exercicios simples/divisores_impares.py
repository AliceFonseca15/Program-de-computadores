def divisores(num,div):
    if div == 1:
        return 1
    else:
        if div % 2 != 0 and num % div == 0:
            return 1 + divisores(num,div - 1)
        else:
            return 0 + divisores(num,div - 1)


def divisores_impares(num):
    print(divisores(num,num))
numero = int(input())
n = divisores_impares(numero)