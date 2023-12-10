user = input("Username : ")

data = {
  "manu":{'super_rebirth': 1, 'point': 77854, 'upgrade': 13, 'rebirth': 2,"mega_rebirth":1,"ultra_rebirth":1,"ff":1},
  "neven":{'ultra_rebirth': 1, 'rebirth': 1, 'ff': 1, 'super_rebirth': 1111, 'point': 0, 'upgrade': 1, 'mega_rebirth': 287},
  "new":{'ultra_rebirth': 1, "rebirth": 1, "ff": 1, 'super_rebirth': 1, 'point': 0, 'upgrade': 1, 'mega_rebirth': 1}
}

if user not in data:
  user = "new"

point = data[user]["point"]
upgrade = data[user]["upgrade"]
rebirth = data[user]["rebirth"]
superRebirth = data[user]["super_rebirth"]
megaRebirth = data[user]["mega_rebirth"]
ultraRebirth = data[user]["ultra_rebirth"]
ff = data[user]["ff"]
executeCount = 0



upgradesList = {
  1:[1, 100],
  2:[2, 125],
  3:[5, 150],
  4:[8, 175],
  5:[12, 200],
  6:[18, 250],
  7:[28, 300],
  8:[42, 350],
  9:[60, 400],
  10:[110, 1000],
  11:[180, 1300],
  12:[240, 1700],
  13:[350, 3000],

  14:[500, 10000],
  15:[700, 18000],
  16:[1000, 45000],
  17:[1500, 60000],
  18:[2500, 120000],
  19:[4000, 180000],
  20:[6500, 250000],
  21:[10000, 400000],
  22:[16000, 600000],
  23:[28000, 900000],
  24:[50000, 1.4e6],
  25:[80000, 2.5e6],
  
  26:[130000, 4e6],
  27:[250000, 7e6],
  28:[400000, 10e6],
  29:[650000, 25e6],
  30:[1e6, 40e6],
  31:[3e6, 70e6],
  32:[5e6, 100e6],
  33:[9e6, 200e6],
  34:[15e6, 350e6],
  35:[25e6, 500e6],
  36:[50e6, 700e6],
  
  37:[300e6, 1e9],
  38:[600e6, 3e9],
  39:[1e9, 9e9],
  40:[4e9, 27e9],
  41:[12e9, 81e9],

  42:[60e9, 1e9],
  43:[200e9, 5e12],
  44:[1e12, 25e12],
  45:[5e12, 100e12],
  46:[30e12, 500e12],
  47:[100e12, 2e15],
  48:[400e12, 10e15],
  49:[1e15, 50e15],

  50:[5e15, 200e15],
  51:[15e15, 1e18],
  52:[50e15, 10e18],
  53:[250e15, 100e18],
  54:[1e18, 1e21],
  55:[11e18, 10e21],
  56:[120e18, 100e21],

  57:[1.3e21, 1e24],
  58:[14e21, 10e24],
  59:[150e21, 100e24],
  60:[1.6e24, 1e27],
  61:[18e24, 10e27],
  62:[200e24, 100e27],
  63:[2.2e27, 1e30],
  64:[24e27, 10e30],
  65:[260e27, 100e30],
  66:[3e30, 1e33],
  67:[33e30, 10e33],
  68:[360e30, 100e33]
}

try:
  f""
except:
  platform = "calculator"
else:
  platform = "computer"


for i in upgradesList:
  upgradesList[i][1] *= upgradesList[i][0]
  if platform == "calculator":
    upgradesList[i][1] //= 2

rebirthList = {
  1: 10000,
  5: 100000,
  25: 1e6,
  100: 1e7,
  800: 1e9,
  6000: 1e11,
  24000: 1e13,
  120000: 1e15,
  500000: 1e17,
  4e6: 1e19,
  20e6: 1e21,
  100e6: 1e24,
  1e9: 1e27,
  10e9: 1e30,
  1e12: 1e35,
  100e12: 1e39,
  10e15: 1e44,
  1e18: 1e50,
  100e18: 1e56,
  10e21: 1e62,
  10e24: 1e70,
  10e27: 1e78,
  100e30: 1e86
}

superRebirthList = {
  1: 500,
  3: 15000,
  10: 100000,
  100: 1e7,
  1000: 1e9,
  10000: 1e11,
  100000: 1e14,
  1e6: 1e16,
  10e6: 1e19,
  100e6: 1e22,
  1e9: 1e25,
  10e9: 1e28,
  100e9: 1e30,
  1e12: 1e33
}

megaRebirthList = {
  3: 500,
  8: 5000,
  25: 25000,
  75: 150000,
  200: 750000,
  500: 1e7,
  2000: 1e8,
  6000: 1e9,
  24000: 1e11,
  100000: 1e13
}

ultra_reb = {
  5: 1000,
  12: 10000,
  30: 100000,
  80: 1e6
}

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

while True:
  if executeCount % 10 == 0:
    for i in range(5):
    inp = input(("- " if upgradesList[upgrade][1]<point else "")+back(upgradesList[upgrade+1][0])+":"+back(upgradesList[upgrade][1])+"p\n"+("- " if upgradesList[upgrade+1][1]<point else "")+back(upgradesList[upgrade+2][0])+":"+back(upgradesList[upgrade+1][1])+"p\n"+("- " if upgradesList[upgrade+2][1]<point else "")+back(upgradesList[upgrade+3][0])+":"+back(upgradesList[upgrade+2][1])+"p\n"+("- " if upgradesList[upgrade+3][1]<point else "")+back(upgradesList[upgrade+4][0])+":"+back(upgradesList[upgrade+3][1])+"p\n"+("- " if upgradesList[upgrade+4][1]<point else "")+back(upgradesList[upgrade+5][0])+":"+back(upgradesList[upgrade+4][1])+"p\nPoint : "+back(point)+" -->")
    executeCount += 1
  else:
    inp = input("Point : "+str(back(point))+" -->")

  if inp == "u":
    while upgradesList[upgrade][1] <= point:
      upgrade += 1
      executeCount = 0
    if executeCount == 0:
      point -= upgradesList[upgrade-1][1]

  elif inp == "r":
    a = sorted([("- " if rebirthList[i]<point else "")+("("+str(back(eval(i)))+") " if eval(i)>=1e6 else "")+i+"r:"+back(rebirthList[i])+" p" for i in rebirthList],key=lambda x:abs(eval(x[(x.index(")")+2 if ")" in x else 0):x.index("r")])))
    b = a[:(len(a)+1)//2]
    c = a[(len(a)+1)//2:]
    d = []
    for i in range(len(b)):
      try:
        d.append(str(b[i]) + "   " + str(c[i]))
      except:
        d.append(str(b[i]))
      
    print(*d, sep="\n")

    if (inp:=input("-->")) in [i for i in rebirthList]:
      if rebirthList[inp] <= point:
        point = 0
        upgrade = 1
        rebirth += eval(inp) * ff
      else:
        print(str(back(rebirthList[inp])) + " points required")

  elif inp == "sr":
    a = sorted([("- " if superRebirthList[i]<rebirth else "")+("("+str(back(eval(i)))+") " if eval(i)>=1e6 else "")+i+"sr:"+back(superRebirthList[i])+" r" for i in superRebirthList],key=lambda x:abs(eval(x[(x.index(")")+2 if ")" in x else 0):x.index("sr")])))
    b = a[:(len(a)+1)//2]
    c = a[(len(a)+1)//2:]
    d = []
    for i in range(len(b)):
      try:
        d.append(str(b[i]) + "   " + str(c[i]))
      except:
        d.append(str(b[i]))

    print(*d, sep="\n")

    if (inp:=input("-->")) in [i for i in superRebirthList]:
      if superRebirthList[inp] <= rebirth:
        point = 0
        upgrade = rebirth = 1
        superRebirth += eval(inp) * ff
      else:
        print(str(back(superRebirthList[inp])) + " rebirth required")

  elif inp == "mr":
    a = sorted([("- " if megaRebirthList[i]<superRebirth else "")+("("+str(back(eval(i)))+") " if eval(i)>=1e6 else "")+i+"mr:"+back(megaRebirthList[i])+" sr" for i in megaRebirthList],key=lambda x:abs(eval(x[(x.index(")")+2 if ")" in x else 0):x.index("mr")])))
    b = a[:(len(a)+1)//2]
    c = a[(len(a)+1)//2:]
    d = []
    for i in range(len(b)):
      try:
        d.append(str(b[i]) + "      " + str(c[i]))
      except:
        d.append(str(b[i]))

    print(*d, sep="\n")

    if (inp:=input("-->")) in [i for i in megaRebirthList]:
      if megaRebirthList[inp] <= superRebirth:
        point = 0
        upgrade = rebirth = superRebirth = 1
        megaRebirth += eval(inp) * ff
      else:
        print(str(back(megaRebirthList[inp])) + " super rebirth required")

  elif inp == "ur":
    print(*sorted([("- " if ultra_reb[i]<megaRebirth else "")+("("+str(back(eval(i)))+") " if eval(i)>=1e6 else "")+i+"ur:"+back(ultra_reb[i])+" mr" for i in ultra_reb],key=lambda x:abs(eval(x[(x.index(")")+2 if ")" in x else 0):x.index("ur")]))),sep="\n")
    
    if (inp:=input("-->")) in [i for i in ultra_reb]:
      if ultra_reb[inp] <= megaRebirth:
        point = 0
        upgrade = rebirth = superRebirth = megaRebirth = 1
        ultraRebirth += eval(inp) * ff
      else:
        print(str(back(ultra_reb[inp])) + " mega rebirth required")

  elif inp == "ff":
    if ultraRebirth >= 1000:
      if input(str(ff) + "->"+str(ff*2) + "ff ?") in ["y", "yes", "ok"]:
        point = 0
        upgrade = rebirth = superRebirth = megaRebirth = ultraRebirth = 1
        ff *= 2
    else:
      print("1000 ultra rebirth required")

  elif inp=="s":
    unlocked_upgrade = []
    if ff>1:unlocked_upgrade+="fumsr"
    elif ultraRebirth>1:unlocked_upgrade+="umsr"
    elif megaRebirth>1:unlocked_upgrade+="msr"
    elif superRebirth>1:unlocked_upgrade+="sr"
    elif rebirth>1:unlocked_upgrade+="r"
    print("Upgrade : "+str(back(upgradesList[upgrade][0])))
    if "r" in unlocked_upgrade:print("Rebirth :",back(rebirth))
    if "s" in unlocked_upgrade:print("Super rebirth :",back(superRebirth))
    if "m" in unlocked_upgrade:print("Mega rebirth :",back(megaRebirth))
    if "u" in unlocked_upgrade:print("Ultra rebirth :",back(ultraRebirth))
    if "f" in unlocked_upgrade:print("ff :",back(ff))
    print("Total :",back(upgradesList[upgrade][0]*rebirth*superRebirth*megaRebirth*ultraRebirth*ff))

  elif inp=="h":print("Commands :\n[u]pgrade\n[r]ebirth\n[sr]super rebirth\n[mr]mega rebirth\n[ur]ultra rebirth\n[ff]\n[h]elp\n[s]tats\n[e]nd")

  elif inp=="e":break
  
  else:
    executeCount += 1
    point += upgradesList[upgrade][0] * rebirth * superRebirth * megaRebirth * ultraRebirth * ff

data={
  "point":point,
  "upgrade":upgrade,
  "rebirth":rebirth,
  "super_rebirth":superRebirth,
  "mega_rebirth":megaRebirth,
  "ultra_rebirth":ultraRebirth,
  "ff":ff
}
print(data)