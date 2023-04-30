def sandbox_creation(nom_sandbox,sandbox_data,v,username):
    if (nom_sandbox, username) in sandbox_data:
        print("Sandbox already exist")
    else:
        sandbox_data[nom_sandbox,username] = {1:"print('Start')"}
        print("Sandbox number",v,"have been created by",username,"with name :",nom_sandbox)
        sandbox_list[v] = ("Sandbox numéro "+str(v)+" créé par "+username+" nommé '"+nom_sandbox)
        if username in sandbox_user:
            sandbox_user[username]=sandbox_user[username]+"\n"+nom_sandbox
        else:
            sandbox_user[username]=nom_sandbox
    return


def sandbox_start(nom_sandbox,username):
    if (nom_sandbox, username) not in sandbox_data:
        print("Sandbox not found")
    else:
        print("Your sandbox '",nom_sandbox,"' is ready to use, enter 'ø' to stop")
        sandbox(sandbox_data,boucle2)
    return

def sandbox_run(username,nom_sandbox,sandbox,data):
    if (nom_sanbox,username) not in sandbox_data:
        print("Sandbox not found")
    else:
        print("Coming soon")


def sandbox(sandbox_data,boucle2):
    while boucle2:
        l=len(sandbox_data[nom_sandbox,username])+1
        message=input("-> ")
        if message.find("ø")>-1:
            print("Sandbox ended, enter /sr",nom_sandbox,"to run your code and /sm",nom_sandbox,"to modify your code")
            boucle2=False
        else:
            sandbox_data[nom_sandbox,username][l]=message
            for k in range(1,len(sandbox_data[nom_sandbox,username])+1):
                print(sandbox_data[nom_sandbox,username][k])


def temporary_sandbox(username):
    print("Coming soon")


k=0
l=1
v=1
boucle2=True
sandbox_list={}
sandbox_data={}
sandbox_user={}
nom_sandbox=""
username=input("Username : ")
boucle=True


while boucle:
    message=input("-> ")
    if message.find("/sc")==0:
        message_list=message.split(" ")
        nom_sandbox=message_list[1]
        sandbox_creation(nom_sandbox,sandbox_data,v,username)
        v+=1
        
    elif message.find("/sf")==0:
        print("Sandbox created, press 'ø' to end sandbox, it will be destroy")
        temporary_sandbox(username)
        
    elif message.find("/ss")==0:
        message_list=message.split(" ")
        nom_sandbox=message_list[1]
        sandbox_start(nom_sandbox,username)
        
    elif message.find("/sr")==0:
        message_list=message.split(" ")
        nom_sandbox=message_list[1]
        sandbox_run(username,nom_sandbox,sandbox_data)
        
    elif message=="/shelp" or message=="/s help":
        print(" - /sf : Enter in a temporary sandbox\n - /sc (sandbox name) : Create a sandbox\n - /ss (sandbox name) : Enter a sandbox\n - /sr (sandbox name) : Run code from sandbox in shell\n - /sh (sandbox name) : Show a sandbox\n - /sl : Show list of sandbox you have")
        
    elif message.find("/sh")==0:
        message_list=message.split(" ")
        nom_sandbox=message_list[1]
        if (nom_sandbox,username) in sandbox_data:
            for k in range(1,len(sandbox_data[nom_sandbox,username])+1):
                print(sandbox_data[nom_sandbox,username][k])
        else:
            print("Sandbox not found")

    elif message=="/sl":
        print(sandbox_user[username])
        
    else:
        boucle=False