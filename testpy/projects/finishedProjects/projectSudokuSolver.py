sudoku=[]
possible=dic={}
chc=0
error=False
for i in range(81):
    possible[i+1]=""
casenum=[[1,2,3,10,11,12,19,20,21],[4,5,6,13,14,15,22,23,24],[7,8,9,16,17,18,25,26,27],[28,29,30,37,38,39,46,47,48],[31,32,33,40,41,42,49,50,51],[34,35,36,43,44,45,52,53,54],[55,56,57,64,65,66,73,74,75],[58,59,60,67,68,69,76,77,78],[61,62,63,70,71,72,79,80,81]]
#for i in range(1,10):
    #sudoku.append(input(f"Line {i} : "))
    #sudoku.append("123456789")
detail=False
#sudoku=['761583492', '943276851', '852419367', '174325986', '689147235', '235968174', '326794518', '518632749', 497851623',] #full
#sudoku=['?61?834?2', '9432????1', '?524?9367', '1?4325986', '?89147235', '235??8174', '3?6?9?518', '5186?2749', '497???6?3'] #modified full
#sudoku=['??96??1??', '?1?7???8?', '35??1????', '5?????6??', '????42??1', '??3????7?', '??5??6?1?', '??68??3?4', '?8147?2??'] #hard
#sudoku=['5?84?2??1', '3??951?78', '1??6????5', '?34?89?2?', '???123?97', '?19746??3', '??1????6?', '?268????4', '?7?????1?'] #easy
sudoku=['91?42?5?8', '?8???????', '????8?197', '3?5???9??', '?26?4?8?1', '89?????73', '???13?6??','???5?????','5???64???'] #medium
#sudoku=[]

x=0
for i in sudoku:
    for j in i:
        x+=1
        for k in range(9):
            colo=x%(k+1)
        if colo==0:colo=9
        if x==28 or x==55:
            print("-----------")
        if colo==4 or colo==7:
            print(f"|{j}",end="")
        elif colo!=9:
            print(f"{j}",end="")
        else:
            print(f"{j}")

while chc<2 and not error:
    
    a=0
    for i in sudoku:
        a+=i.count("?")
    if a==0:break
    
    case=["","","","","","","","",""]
    col=["","","","","","","","",""]
    
    for i in sudoku:
        for j in range(9):
            col[j]+=i[j]
            
    x=0
    for i in sudoku:
        for j in i:
            x+=1
            for k in casenum:
                if x in k:
                    case[casenum.index(k)]+=j
                
    x=0
    for i in sudoku:
        for j in i:
            x+=1
            for k in range(0,10):
                if x>9*k:
                    lign=sudoku[k]
                    numlign=k+1
                if k!=0:
                    colo=col[x%k-1]
                    numcolo=x%k
            for k in casenum:
                if x in k:
                    cas=case[casenum.index(k)]
                    numcas=casenum.index(k)+1
            if j=="?":
                #print(f"({x}) {j} _{lign}_ |{colo}| ❏{cas}❏")
                possible[x]=""
                for l in "123456789":
                    if l not in lign and l not in colo and l not in cas:
                        if l not in possible[x]:
                            possible[x]+=l
    ch=False
    x=0
    for i in sudoku:
        for j in i:
            x+=1
            if j=="?":
                for k in range(0,10):
                    if x>9*k:
                        lign=sudoku[k]
                        numlign=k+1
                        if len(lign)>9:lign=lign[:9]
                        for m in lign:
                            if lign.count(m)>1 and m!="?":
                                print(f"Error {m} in {lign}, multiple number in line")
                                error=True
                    if k!=0:
                        colo=col[x%k-1]
                        numcolo=x%k
                        if numcolo==0:numcolo=9
                        for m in colo:
                            if colo.count(m)>1 and m!="?":
                                print(f"Error {m} in {colo}, multiple number in row")
                                error=True
                for k in casenum:
                    if x in k:
                        cas=case[casenum.index(k)]
                        numcas=casenum.index(k)+1
                        numincas=k.index(x)+1
                        for m in cas:
                            if cas.count(m)>1 and m!="?":
                                print(f"Error {m} in {cas}, multiple number in case")
                                error=True
                if ch:continue
                pcolo=0
                numpossible=[]
                impossible=""
                for k in lign:
                    pcolo+=1
                    if pcolo!=numcolo and k=="?":
                        pnum=9*numlign-9+pcolo
                        numpossible.append(pnum)
                    if k!="?":
                        impossible+=k
                for k in numpossible:
                    for l in possible[k]:
                        if l not in impossible:
                            impossible+=l
                for k in possible[x]:
                    if k not in impossible:
                        if detail:
                            print(f"N°{x}, possible[x] is {possible[x]} and impossible is {impossible}, soluce is {k} (in line)")
                        sudoku[numlign-1]=sudoku[numlign-1][:numcolo-1]+k+sudoku[numlign-1][numcolo:]
                        break
                        ch=True
                if ch:continue
                plign=0
                numpossible=[]
                impossible=""
                for k in colo:
                    plign+=1
                    if plign!=numlign and k=="?":
                        pnum=9*plign-9+numcolo
                        numpossible.append(pnum)
                    if k!="?":
                        impossible+=k
                for k in numpossible:
                    if k==0:continue
                    for l in possible[k]:
                        if l not in impossible:
                            impossible+=l
                for k in possible[x]:
                    if k not in impossible:
                        sudoku[numlign-1]=sudoku[numlign-1][:numcolo-1]+k+sudoku[numlign-1][numcolo:]
                        if detail:
                            print(f"N°{x}, possible[x] is {possible[x]} and impossible is {impossible}, soluce is {k} (in row)")
                            print(numpossible)
                        ch=True
                        break
                if ch:continue
                pcas=0
                numpossible=[]
                impossible=""
                for k in cas:
                    pcas+=1
                    if pcas!=numincas and k=="?":
                        pnum=casenum[numcas-1][pcas-1]
                        numpossible.append(pnum)
                        #print(x,pnum,numcas,casenum[numcas-1])
                    if k!="?":
                        impossible+=k
                for k in numpossible:
                    if k==0:continue
                    for l in possible[k]:
                        if l not in impossible:
                            impossible+=l
                if x==80:
                    print(numpossible)
                    print(possible[71])
                    print(impossible)
                for k in possible[x]:
                    if k not in impossible:
                        sudoku[numlign-1]=sudoku[numlign-1][:numcolo-1]+k+sudoku[numlign-1][numcolo:]
                        if detail:
                            print(f"N°{x}, possible[x] is {possible[x]} and impossible is {impossible}, soluce is {k} (in case)")
                        ch=True
                        break
    
    for i in range(9):
        if len(sudoku[i])>9:
            sudoku[i]=sudoku[i][:9]
    if not ch:
        chc+=1
        ch=False
        
    #print("Sudoku : ")
    #print(*sudoku,sep='\n')
if error:
    print("Error :")
else:
    print("Sudoku solved : ")
x=0
for i in sudoku:
    for j in i:
        x+=1
        for k in range(9):
            colo=x%(k+1)
        if colo==0:colo=9
        if x==28 or x==55:
            print("-----------")
        if colo==4 or colo==7:
            print(f"|{j}",end="")
        elif colo!=9:
            print(f"{j}",end="")
        else:
            print(f"{j}")