l=[]
while True:
    if (nombre:=int(input("Entrez un nombre entier : "))) < 3:
        print("Choisissez un nombre supérieur à 2.")
        continue
    for i in range(2, nombre - 1):
        if nombre % i == 0:
            if i not in l:
                l.append(i)
    if l == []:
        print("Aucun diviseur")
    else:
        print(*l)
    l = []