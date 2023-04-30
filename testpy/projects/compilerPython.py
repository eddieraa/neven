sd={"test":{"test":["print('Hello world')","a=2","print(a)"]}}
user=input("Username : ")
while True:
  if (inp:=input("->"))=="ui":
    if user in sd:
      print("Sandbox : ",*sd[user],sep="\n - ")
      if (si:=input("Sandbox info -> ")) in sd[user]:
        td={}
        for e,i in enumerate(sd[user][si]):
          td[e+1]=i
        print("----------",*[str(i)+": "+td[i] for i in td]+["----------"],sep="\n")
      else:
        print("Sandbox not found")
    else:
      print("No sandbox")
  elif inp=="sm":
    if user in sd:
      print("Sandbox : ",*sd[user],sep="\n - ")
      if (sm:=input("--> ")) in sd[user]:
        td={}
        for e,i in enumerate(sd[user][sm]):
          td[e+1]=i
        print("Enter [e] to end, [d] to delete a line and [a] to add a line","----------",*[str(i)+": "+td[i] for i in td],sep="\n")
        while True:
          c=input(str(len(td)+1)+": ")
          if c=="e":
            print("[se] to execute sandbox")
            break
          elif c=="d":
            if (c:=input("--> ")).isdigit() and int(c) in td:
              sd[user][sm].pop(int(c)-1)
              td={}
              for e,i in enumerate(sd[user][sm]):
                td[e+1]=i
              print("----------",*[str(i)+": "+td[i] for i in td],sep="\n")
            else:
              print("Error")
          elif c=="a":
            if (c:=input("--> ")).isdigit() and int(c) in td:
              sd[user][sm]=sd[user][sm][:int(c)-1]+[input(c+" :")]+sd[user][sm][int(c)-1:]
              td={}
              for e,i in enumerate(sd[user][sm]):
                td[e+1]=i
              print("----------",*[str(i)+": "+td[i] for i in td],sep="\n")
            else:
              print("Error")
          else :
            sd[user][sm].append(c)
            td[len(td)+1]=c
      else:print("Sandbox not found")
    else:
      print("No sandbox")
  elif inp=="se":
    if user in sd:
      print("Sandbox : ",*sd[user],sep="\n - ")
      if (sm:=input("--> ")) in sd[user]:
        for i in sd[user][sm]:pass
  elif inp=="ns":
    nsn=input("New sandbox name : ")
    if user not in sd:
      sd[user]={nsn:[]}
    if nsn not in sd[user]:
      sd[user][nsn]=[]
    else:
      print(nsn,"already exist")
  elif inp=="ca":
    user=input("Username : ")
  elif inp=="e":break
print(sd)