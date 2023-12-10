def lunnule(integer):
    #la fonction lunnule etant une copie de la fonction int(), permettant de convertir un string en integer
    b,stri,chif=[],"",["0","1","2","3","4","5","6","7","8","9"]
    if type(integer) is int:return integer
    elif type(integer) is float:integer=str(integer).split(".")[0]
    elif integer.endswith(".0"):integer=integer[:-2]
    elif type(integer) is not str:raise TypeError("La fonction Lunnule ne prend en compte que les variables de type string")
    for i in range(len(integer)):
        if integer[i] not in chif:
            if integer[i]==".":break
            else:raise TypeError(f"Impossible de convertir '{integer[i]}' en integer")
        b.append(chif.index(integer[i]))
    for i in range(len(b)):b[i]*=10**(len(b)-i-1)
    return sum(b) 
