while True:
    frase = input()
    if frase == "*": 
        break

    palavras = frase.split()  

    letra = palavras[0][0].lower()

    tautograma = True  

    for palavra in palavras:
        if palavra[0].lower() != letra:  
            tautograma = False
            break
        
    if tautograma:
        print("Y")
    else:
        print("N")