from random import *
list_user={'Admin':{'ID':1,'Password':'1234','Statut':'Admin','Data':{}}}
list_ID=[]
connection=False
while True:
    inp=input("->")
    if inp=="command_list":
        print("add_user, search_user, user_list, disconnect, connect, change_password, user_info")
    if inp=="add_user":
        a=0
        while a==0:
            a=1
            username=input("Entrez votre nom : ")
            if username in list_user:
                print("Nom déjà pris")
                a=0
        password=input("Choisissez un mot de passe : ")
        a=0
        while a==0:
            a=1
            ID=randint(0,1000**3)
            if ID in list_ID:
                a=0
        list_user[username]={"ID":ID,"Password":password,"Statut":"User","Data":{}}
        list_ID.append(ID)
    if inp=="search_user":
        username=input("Entrez le nom : ")
        found=False
        if username in list_user:
            print(f"Utilisateur trouvé :\nNom : {username}\nID : {list_user[username]['ID']}")
        else:
            print("Utilisateur introuvable")
    if inp=="user_list":
        for i in list_user:
            print(f"Nom : {i}, ID : {list_user[i]['ID']}")
    if inp=="disconnect":
        if connection==False:
            print("Vous n'étiez pas connecté")
            continue
        elif type(connection) is list:
            print(f"Déconnecté du compte {connection[len(connection)-1]} depuis le compte Admin")
            if len(connection)==2:
                connection=connection[0]
            else:
                connection.pop(len(connection)-1)
        else:
            print(f"Déconnecté du compte {connection}")
            connection=False
    if inp=="connect":
        if connection!=False:
            if type(connection) is list:
                username=input("Connection en tant qu'admin, nom d'utilisateur : ")
                if username in list_user:
                    connection+=username
                else:
                    print("Utilisateur introuvable")
                continue
            elif list_user[connection]["Statut"]=="Admin":
                username=input("Connection en tant qu'admin, nom d'utilisateur : ")
                if username in list_user:
                    connection=[connection,username]
                else:
                    print("Utilisateur introuvable")
                continue
            else:
                print(f"Vous êtes déjà connecté en tant que {connection}")
                continue
        username=input("Nom d'utilisateur : ")
        found=False
        password_verification=False
        Try=0
        if username in list_user:
            while password_verification==False:
                password=input("Entrez votre mot de passe : ")
                if password==list_user[username]["Password"]:
                    connection=username
                    password_verification=True
                    print(f"Vous êtes maintenant connecté en tant que {username}")
                else:
                    if Try==2:
                        print("Echec de l'authentification")
                        break
                    else:
                        print("Mot de passe incorrect, réessayez")
                        Try+=1
        else:
            print("Utilisateur introuvable")
    if inp=="change_password":
        if connection==False:
            print("Vous n'êtes pas connecté")
        elif type(connection) is list:
            user=input(f"Vous êtes connecté sur les comptes {connection}, sur lequel voulez-vous changer de mot de passe ? : ")
            if user not in connection:
                print("Utilisateur introuvable")
            else:
                password=input("Entrez le nouveau mot de passe : ")
            list_user[user]["Password"]=password
        else:
            password=input("Entrez votre nouveau mot de passe : ")
            list_user[a]["Password"]=password
    if inp=="user_info":
        if connection==False:
            print("Vous n'êtes pas connecté")
            continue
        a=0
        if type(connection) is list:
            a=2
        elif list_user[connection]["Statut"]=="Admin":
            a=2
        if a==2:
            a=input("Sur quel utilisateur voulez-vous des information ? : ")
            if a=="tous":
                for i in list_user:
                    print(f"Nom : {i}, ID : {list_user[i]['ID']}, Mot de passe : {list_user[i]['Password']}, Statut : {list_user[i]['Statut']}")
            else:
                if a not in list_user:
                    print("Utilisateur introuvable")
                else:
                    print(f"Nom : {a}\nID : {list_user[a]['ID']}\nMot de passe : {list_user[a]['Password']}\nStatut : {list_user[a]['Statut']}")
        else:
            print(f"Nom : {connection}\nID : {list_user[connection]['ID']}\nMot de passe : {list_user[connection]['Password']}\nStatut : {list_user[connection]['Statut']}")
    if inp=="end":break