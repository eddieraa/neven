def calcul(n):
    if n.count("=")>0:
        return calcul(n.split("=")[0])==calcul(n.split("=")[1])
    n=n.replace("pi","3.141592653")
    if n.count("+")!=0:
        return float(n.split("+")[0])+float(n.split("+")[1])
    elif n.count("/")!=0:
        return float(n.split("/")[0])/float(n.split("/")[1])
    elif n.count("**")!=0:
        return float(n.split("**")[0])**float(n.split("**")[1])
    elif n.count("*")!=0:
        return float(n.split("*")[0])*float(n.split("*")[1])
    elif n.count("-")!=0:
        return float(n.split("-")[0])-float(n.split("-")[1])
    else:
        return float(n)