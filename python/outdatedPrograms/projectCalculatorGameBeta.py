from math import *
from random import *
#Do not modify code, it could corrupt the entire program.
IM=1e6
IB=1e9
IT=1e12
money=0
upgrade=1
rebirth=1
clicks=0
prix_up=10
fact_up=1
prix_reb=IM
fact_reb=1
gain=1
vr=0
inventory=[]
ent=""
al=sum([money,upgrade,rebirth,clicks,prix_reb])
pet_dict={"common":1.5,"uncommon":2.5,"rare":4,"mythique":10,"legendaire":25,"ultra":100,"god":1000,}

data=""
#data=""
#data=""
#data=""
#data=""

if data!="":
    data_sp=data.split(",")
    data_add=float(data_sp[0]) + float(data_sp[1]) + float(data_sp[2]) + float(data_sp[3]) + float(data_sp[4]) + float(data_sp[5])
    for i in range(len(data_sp)-8):
        data_add+=float(data_sp[i+6])
    vr=[float(data_sp[0])/81 , int(float(data_sp[1])/3902) , int(float(data_sp[3])/5167) , int(float(data_sp[5])/672)]
    vr=sum(vr)
    if data_add*int(data_sp[len(data_sp)-2])!=int(float(data_sp[len(data_sp)-1])):
        raise Exception("Data corrupted")
    else:
        money=float(data_sp[0])/81
        upgrade=int(float(data_sp[1])/3902)
        fact_up=float(data_sp[2])/9988
        rebirth=int(float(data_sp[3])/5167)
        fact_reb=float(data_sp[4])/45678
        clicks=int(float(data_sp[5])/672)
        for i in range(len(data_sp)-8):
            inventory.append(data_sp[i+6])
        al=sum([float(data_sp[0])/81,int(float(data_sp[1])/3902),int(float(data_sp[3])/5167),int(float(data_sp[5])/672)])
if al!=1000003 and al!=vr:raise Exception("Program is corrupted")
def back(num):
  if   num>=1e90:return str(round(num/1e90,2))+" Nvg"
  elif num>=1e87:return str(round(num/1e87,2))+" Ocvg"  
  elif num>=1e84:return str(round(num/1e84,2))+" Spvg"  
  elif num>=1e81:return str(round(num/1e81,2))+" Sxvg"  
  elif num>=1e78:return str(round(num/1e78,2))+" Qivg"  
  elif num>=1e75:return str(round(num/1e75,2))+" Qavg"  
  elif num>=1e72:return str(round(num/1e72,2))+" Tvg"
  elif num>=1e69:return str(round(num/1e69,2))+" Dvg"  
  elif num>=1e66:return str(round(num/1e66,2))+" Uvg"  
  elif num>=1e63:return str(round(num/1e63,2))+" Vg"  
  elif num>=1e60:return str(round(num/1e60,2))+" Nd" 
  elif num>=1e57:return str(round(num/1e57,2))+" Ocd"  
  elif num>=1e54:return str(round(num/1e54,2))+" Spd"  
  elif num>=1e51:return str(round(num/1e51,2))+" Sxd"  
  elif num>=1e48:return str(round(num/1e48,2))+" Qid" 
  elif num>=1e45:return str(round(num/1e45,2))+" Qad"  
  elif num>=1e42:return str(round(num/1e42,2))+" Td"  
  elif num>=1e39:return str(round(num/1e39,2))+" Dd"  
  elif num>=1e36:return str(round(num/1e36,2))+" Ud"  
  elif num>=1e33:return str(round(num/1e33,2))+" D"  
  elif num>=1e30:return str(round(num/1e30,2))+" N" 
  elif num>=1e27:return str(round(num/1e27,2))+" Oc"  
  elif num>=1e24:return str(round(num/1e24,2))+" Sp"  
  elif num>=1e21:return str(round(num/1e21,2))+" Sx"
  elif num>=1e18:return str(round(num/1e18,2))+" Qi"
  elif num>=1e15:return str(round(num/1e15,2))+" Qa"  
  elif num>=1e12:return str(round(num/1e12,2))+" T"  
  elif num>=1e9: return str(round(num/1e9 ,2))+" B"  
  elif num>=1e6: return str(round(num/1e6 ,2))+" M"
  else:          return str(round(num     ,2))
def command_list():
    print("Commands :")
    print(" - shop : Show shop")
    print(" - inv : Show pets")
    print(" - end : Stop the game")
    print(" - stats : Show stats")
    print(" - delpet : Delete a pet")
    print(" - delw : Delete worst(s) pet")
    print(" - eqbest : Equip bests pets")
    print(" - help : Get list of commands")
    print("")
def stats():
    print(f"banque : {back(money)}$")
    print(f"gain : {back(gain)}$")
    print(f"upgrade : {back(upgrade)}")
    print(f"rebirth : {back(rebirth)}")
    print(f"pet : {back(sum([pet_dict[inventory[0]] if len(inventory)>0 else 1,pet_dict[inventory[1]] if len(inventory)>1 else 0,pet_dict[inventory[2]] if len(inventory)>2 else 0,]))}")
    for i in inventory:
        print(i)
    print("clicks :",back(clicks))
command_list()
stats()
while True:
    prix_up=int(10*upgrade*fact_up)
    prix_reb=int(IM*rebirth*fact_reb)
    ent=input("bank :"+str(money)+"$ -> ")
    if ent=="end" or ent=="stats":
        stats()
        if ent=="end":
            sp_data=(money*81)+(upgrade*3902)+(fact_up*9988)+(rebirth*5167)+(fact_reb*45678)+(clicks*672)
            for i in range(len(inventory)):sp_data+=float(inventory[i])
            d=randint(1,9999)
            data=str(float(money*81))+","+str(float(upgrade*3902))+","+str(float(fact_up*9988))+","+str(float(rebirth*5167))+","+str(float(fact_reb*45678))+","+str(float(clicks*672))
            for i in range(len(inventory)):data+=","+str(inventory[i])
            data+=","+str(d)+","+str(sp_data*d)
            print("")
            print("Data :")
            print(data)
            print("Remontez tout le programme et copiez les datas dans le programme ligne 25")
            break
        else:print("")
    elif ent=="cheat":
        fact_cheat=int(input("-->"))
        rebirth*=fact_cheat
        upgrade*=fact_cheat
    elif ent=="cheatp":
        inventory.append("common")
        inventory.append("mythique")
        inventory.append("ultra")
    elif ent=="help":
        command_list()
    elif ent=="shop":
        print(f"[up]grade :,{back(prix_up)}$, actuel :,{upgrade}")
        print(f"[reb]irth :,{back(prix_reb)}$, actuel :,{rebirth}")
        print("[ce]common egg : 500$")
        print("[re]rare egg : 25000$")
        print("[de]draconic egg : 5M$")
        print("[ge]golden egg : 10B$")
        print("")
    elif ent=="up":
        if money<prix_up:
            print("Not enough money")
        else:
            money-=prix_up
            upgrade+=1
            fact_up+=0.1
            prix_up=int(10*upgrade*fact_up)
        print("upgrade :",upgrade," prochain :",back(prix_up))
        print("")
    elif ent=="reb":
        if money<prix_reb:
            print("Pas assez de money")
            print("")
        else:
            money=0
            upgrade=1
            fact_up=1
            prix_up=10
            rebirth+=1
            prix_reb=int(IM*rebirth*fact_reb)
            fact_reb+=0.1
        print("rebirth :",rebirth," prochain :",back(prix_reb))
        print("")
    elif ent=="ce":
        inventory.append(choices(["common","uncommon","rare"],weights=[60,30,10])[0])
        money-=500
    elif ent=="re":
        inventory.append(choices(["common","uncommon","rare","mythique"],weights=[40,35,20,5]))
        money-=25000
    elif ent=="de":
        inventory.append(choices(["common","uncommon","rare","mythique","legendaire"],weights=[15,25,45,12,3]))
        money-=IM*5
    elif ent=="ge":
        inventory.append(choices(["uncommon","rare","mythique","legendaire","ultra","god"],weights=[20,40,30,9,0.9,0.1]))
        money-=IB*10
    elif ent=="inv":
        for i in inventory:
            print(i)
    elif ent=="delpet":
        for i in inventory:
            print(i)
        if (c:=input("Which one delete ? ")) in [i for i in range(len(inventory))]:
            inventory.pop(c-1)
    elif ent=="delw":
        if (b:=input("How many pet ? ")) in [i for i in range(len(inventory))]:
            for i in range(b):
                inventory.remove(min(inventory,key=lambda x:pet_dict[x]))
        else:
            print("Error")
    elif ent=="eqbest":
        inventory.sort(reverse=True,key=lambda x:pet_dict[x])
        for i in range(3):print("(equipped) :",inventory(i))
    else:
        print("(+"+str(back(gain:=sum([pet_dict[inventory[0]] if len(inventory)>0 else 1,pet_dict[inventory[1]] if len(inventory)>1 else 0,pet_dict[inventory[2]] if len(inventory)>2 else 0,])*10))+") ",end="")
        money+=gain
        clicks+=1
    if ent in ["ce","re","de","ge"]:
        print("Found an "+inventory[-1]+" pet (x"+str(pet_dict[inventory[-1]])+")")