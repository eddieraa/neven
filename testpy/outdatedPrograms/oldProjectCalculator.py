def convertion_pc(pourcent):
    """Fonction permettant de retirer le caractère '%'"""
    pourcent = pourcent.strip("%")
    return pourcent
        
def calculatrice(calcul):
    """Fonction permettant de résoudre un calcul"""
    if calcul.find("+")>-1:
        calcul_0 = calcul.split("+")
        solution = int(calcul_0[0])+int(calcul_0[1])
        return solution
    elif calcul.find("-")>0:
        calcul_0 = calcul.split("-")
        solution = int(calcul_0[0])-int(calcul_0[1])
        return solution
    elif calcul.find("/")>-1:
        calcul_0 = calcul.split("/")
        solution = int(calcul_0[0])/int(calcul_0[1])
        return solution
    elif calcul.find("*")>-1:
        if calcul.find("*")!=calcul.rfind("*"):
            if calcul.find("%")>-1:
                calcul_0 = calcul.split("**")
                calcul_0[0]=convertion_pc(calcul_0[0])
                solution=(int(calcul_0[0])*0.01)**int(calcul_0[1])
                return solution
            else:
                calcul_0 = calcul.split("**")
                solution = int(calcul_0[0])**int(calcul_0[1])
                return solution
        elif calcul.find("%")>-1:
            if calcul.find("%")!=calcul.rfind("%"):
                calcul_0 = calcul.split("*")
                calcul_0[1]=convertion_pc(calcul_0[1])
                calcul_0[0]=convertion_pc(calcul_0[0])
                solution = int(calcul_0[0])*int(calcul_0[1])*0.0001
                return solution
            else:
                calcul_0=calcul.split("*")
                if calcul_0[0].find("%")>-1:
                    calcul_0[0]=convertion_pc(calcul_0[0])
                    solution=int(calcul_0[0])*int(calcul_0[1])*0.01
                    return solution
                else:
                    calcul_0[1]=convertion_pc(calcul_0[1])
                    solution=int(calcul_0[0])*int(calcul_0[1])*0.01
                    return solution
        else:
            calcul_0 = calcul.split("*")
            solution = int(calcul_0[0])*int(calcul_0[1])
            return solution
    else:
        return int(calcul)
    


print("Types d'opérations :\n - addition : a+b\n - soustraction : a-b\n - division : a/b\n - multiplication : a*b\n - puissance : a**(exposant)\n - vérification : a=b\n - pourcentage : a(%)*b(%) ou a%**(exposant)\n")


boucle = True
while boucle:
    calcul=input("Entrez un calcul : ")
    if calcul.find("=")==-1:
        solution = calculatrice(calcul)
        print(solution)
    else:
        calcul_0=calcul.split("=")
        if calculatrice(calcul_0[0])==calculatrice(calcul_0[1]):
            print("VRAI,",calcul_0[0],"=",calculatrice(calcul_0[0]),"et",calcul_0[1],"=",calculatrice(calcul_0[1]))
        else:
            print("FAUX,",calcul_0[0],"=",calculatrice(calcul_0[0]),"et",calcul_0[1],"=",calculatrice(calcul_0[1]))