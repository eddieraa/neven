def rabs(a):
  return a * -1 if a < 0 else a

def aiter():pass

def rall(a):
  for i in a:
    try:
      a + {}
    except:
      if not i:
        return False
    else:
      if not i or not a[i]:
        return False
  return True

def rany(a):
  for i in a:
    try:
      a + {}
    except:
      if i:
        return True
    else:
      if i or a[i]:
        return True
  return False

def anext():pass


def rbin(a):
  b = ""
  while a >= 1:
    b = str(a%2) + b
    a //= 2
  return "0b" + b

def rbool(a):
  return True if a else False

def breakpoint():pass


def rcallable(a):
  try:
    a()
  except:
    return False
  else:
    return True

#def rclassmethod():pass


#def delattr():pass

def rdict(*b,**a):
  for i in b:
    for i in i:
      a[i[0]] = i[1]
  return a

def rdivmod(a,b):
  return a//b,a%b


def renumerate(*a):
  b = []
  c=1
  for i in a[0]:
    b += " "
    b[-1] = i,c
    try:a[1]
    except:c+=1
    else:c+=a[1]
  return b


def rfilter(a,b):
  c = []
  for i in b:
    if a(i):
      c += " "
      c[-1] = i
  return c

def rfloat(a):
  try:a+1
  except:pass
  else:
    return a/1

def format():pass

def rfrozenset():pass


def rgetattr():pass

def rglobals():pass


def rhasattr():pass

def rhash():pass

def help():pass

def rhex():pass


def rid():pass

def rint(a):
  try:
    a + 1
  except:
    d = {
      "0":0,
      "1":1,
      "2":2,
      "3":3,
      "4":4,
      "5":5,
      "6":6,
      "7":7,
      "8":8,
      "9":9
    }
    b =- 1
    c = 0
    for i in a:
      b += 1
    for i in a:
      c += d[i]*10**b
      b -= 1
    return c
  else:
    return a

def risinstance():pass

def rissubclass():pass

def riter():pass


def rlen(a):
  b = 0
  for i in a:
    b += 1
  return b

def rlist(a):
  b = []
  for i in a:
    b += "b"
    b[-1] = i
  return b


def rmap(a,b):
  return [a(i) for i in b]

def rmax(*a,**b):
  r = a[0]
  if "key" in b:
    for i in a:
      if b["key"](i) > b["key"](r):
        r = i
  else:
    for i in a:
      if i > r:
        r = i
  return r

def memoryview():pass

def rmin(a,b):
  r = a[0]
  if "key" in b:
    for i in a:
      if b["key"](i) < b["key"](r):
        r = i
  else:
    for i in a:
      if i < r:
        r = i
  return r


def rnext():pass


def robject():pass

def roct():pass

def ropen():pass

def rord():pass


def rpow(a,b):
  return a**b

def property():pass


def rrange(*a):
  e = []
  try:
    a[2]
  except:
    try:
      a[1]
    except:
      d = 0
      while d < a[0]:
        e += "o"
        e[-1] = d
        d += 1
    else:
      d = a[0]
      while d < a[1]:
        e += "o"  
        e[-1] = d
        d += 1
  else:
    d = a[0]
    while d < a[1]:
      e += "o"  
      e[-1] = d
      d += a[2]
  return e

def rremove():pass

def rreversed():pass

def rround():pass


def rset():pass

def rsetattr():pass

def slice():pass

def rsorted():pass

def rstr(a):
  b = 10
  c = ""
  lo = {
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9"
    }
  while a%b!=a:
    c = lo[(a%b)*10//b] + c
    b *= 10
  c = lo[(a%b)*10//b] + c
  return c

def rsum(a):
  b = 0
  for i in a:
    b += i
  return b

def rsuper():pass


def rtuple(a):
  b = ()
  for i in a:
    b += "b"
    b[-1] = i
  return b


def vars():pass


def rzip(a,b):
  c = 0
  d = []
  while True:
    try:
      d += "d"
      d[c] = (a[c], b[c])
      c += 1
    except:
      return d[:-1]