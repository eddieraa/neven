txt="ijed dohed ho edoijde ed"

def titl(txt):
    return "".join([chr(ord(i[:1])-32)+i[1:]+" " for i in txt.split()])[:-1]

print(titl(txt))

def titlSFM(txt):
    dic={"a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G","h":"H","i":"I","j":"J","k":"K","l":"L","m":"M","n":"N","o":"O","p":"P","q":"Q","r":"R","s":"S","t":"T","u":"U","v":"V","w":"W","x":"X","y":"Y","z":"Z"}
    t=""
    a=0
    l=[]
    for i in txt:
        if i==" ":
            a+=1
        else:
            try:
                l[a]+=i
            except:
                l+=i
    for i in l:
        t+=dic[i[:1]]+i[1:]+" "
    return t[:-1]

print(titlSFM(txt))