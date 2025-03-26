sec = (input())

a = 0
c = 0
g = 0
t = 0

var_a = 1
var_c = 1
var_g = 1
var_t = 1
if len(sec) == 1:
    print("1")
else:
    for i in range(1, len(sec)):
        if sec[i] == "A":
            if sec[i] == sec[i - 1]:
                var_a += 1
            else:
                var_a = 1
            a = max(a, var_a)
         
        if sec[i] == "C":
            if sec[i] == sec[i - 1]:
                var_c += 1
            else:
                var_c = 1
            c = max(c, var_c)

        if sec[i] == "G": 
            if sec[i] == sec[i - 1]:
                var_g += 1
            else:
                var_g = 1
            g = max(g, var_g)

        if sec[i] == "T":
            if sec[i] == sec[i - 1]:
                var_t += 1
            else:
                var_t = 1
            t = max(t, var_t)


    numero = max(a, c, g, t)

    print(numero)

    





    
    
    

        




    