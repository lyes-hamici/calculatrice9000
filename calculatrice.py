def add(a,b):
    return a + b


def sous(a,b):
    return a - b


def multiplication(a,b):
    return a * b


def division(a,b):
    return a / b


def div_arrondi(a,b):
    return a // b


def puissance(a,b):
    return a ** b


def modulo(a,b):
    return a % b



def calculatrice():
    result = 0
    try:
        print("----------------------------------")

        a = float(input("Choix du premier nombre : "))

        print("----------------------------------")

        signe = str(input("Choix de l'opérateur : "))

        print("----------------------------------")

        b = float(input("Choix du deuxième nombre : "))

    except:
        print("Entrer un nombre correct. ")
        exit()

    if signe == "+":
        result += add(a,b)
    
    elif signe == "-":
        result += sous(a,b)
    

    elif signe == "*":
        result += multiplication(a,b)
    
    elif signe == "/":
        result += division(a,b)
    
    elif signe == "//":
        result += div_arrondi(a,b)
    
    elif signe == "**":
        result += puissance(a,b)
    
    elif signe == "%":
        result += modulo(a,b)

    else :
        print("Opération illégal '",signe, "' Utiliser l'un des éléments suivant : + , - , * , ** , / , // , %.")
        exit()
        
    
    print("----------------------------------")

    print("résultat final :",a,signe,b," = ",result)
    chaine = ""
    chaine += str(a)
    chaine += " "
    chaine += str(signe)
    chaine += " "
    chaine += str(b)
    chaine += " = "
    chaine += str(result)
    
    print("----------------------------------")
    fichier = open("historique.txt", "a")
    fichier.write( chaine + "\n")
    fichier.close()
        

calculatrice()


#Version 4 , avec 3 éléments (1 + 1 * 1) soit a b c ainsi que les signes +,-,etc.

'''def calculatrice():
    result = 0

    print("----------------------------------")
    try:
        a = float(input("Choix du premier nombre : "))

        print("----------------------------------")

        signe = str(input("Choix de l'opérateur : "))

        print("----------------------------------")

        b = float(input("Choix du deuxième nombre : "))

    # premier signe  d'operation
    except ValueError:
        print("Ceci n'est pas un nombre.")
        exit()
        
    if signe == "+":
        result += add(a,b)
    
    elif signe == "-":
        result += sous(a,b)
    

    elif signe == "*":
        result += multiplication(a,b)
    
    elif signe == "/":
        result += division(a,b)
    
    elif signe == "//":
        result += div_arrondi(a,b)
    
    elif signe == "**":
        result += puissance(a,b)
    
    elif signe == "%":
        result += modulo(a,b)

    # ------------------------------------------------------------------------------------------------------------ 

    print("----------------------------------")

    r2 = result

    signe3 = str(input("Choix de l'opérateur entre calcul : "))

    print("----------------------------------")

    c = float(input("Choix du premier nombre : "))

    result3 = 0
    

    # Signe du millieu d'operation  

    if signe3 != "+" or signe3 != "-" or signe3 != "*" or signe3 != "/" or signe3 != "//" or signe3 != "**" or signe3 != "%":
        print("----------------------------------")
        print("opérations illégales :",signe3 ,", essayé l'un des opérateurs suivants : + , - , * , ** , / , // , %.")
 
    elif signe3 == "+":
        result3 += add(r2,result)

    elif signe3 == "-":
        result3 += sous(r2,result)
    

    elif signe3 == "*":
        result3 += multiplication(b,c)
        if signe == "+":
            result3 = add(a,multiplication(b,c))

        elif signe == "-":
            result3 = sous(a,multiplication(b,c))

    
    elif signe3 == "/":
        result3 += division(b,c)
        if signe == "+":
            result3 = add(a,division(b,c))

        elif signe == "-":
            result3 = sous(a,division(b,c))
    
    elif signe3 == "//":
        result3 += div_arrondi(b,c)
        if signe == "+":
            result3 = add(a,div_arrondi(b,c))

        elif signe == "-":
            result3 = sous(a,div_arrondi(b,c))

    elif signe3 == "**":
        result3 += puissance(r2,result)
        if signe == "+":
            result3 = add(a,puissance(b,c))

        elif signe == "-":
            result3 = sous(a,puissance(b,c))

        elif signe == "*":
            result3 = multiplication(a,puissance(b,c))

        elif signe == "/":
            result3 = division(a,puissance(b,c))

        elif signe == "//":
            result3 = div_arrondi(a,puissance(b,c))

        elif signe == "%":
            result3 = modulo(a,puissance(b,c))
        
    
    elif signe3 == "%":
        result3 += modulo(r2,result)

    # ------------------------------------------------------------------------------------------------------------ 

    print("----------------------------------")

    print("résultat final :",a,signe,b,signe3,c," = ",result3)
    
    print("----------------------------------")
        
        

calculatrice()'''