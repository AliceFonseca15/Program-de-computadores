nome = input("")
horas = int(input(""))
valorh = float(input(""))
c = horas * valorh
c2 = "{:.2f}".format(c)
print(nome)
print("R$",c2)