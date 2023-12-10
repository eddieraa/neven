from time import *
s=0
def z(h):return "0"+str(h) if len(str(h))==1 else str(h)
while True:
  print(z(s//3600)+":"+z(s//60-s//3600*60)+":"+z(s-s//60*60))
  #sleep(0.74)
  sleep(1)
  s+=1