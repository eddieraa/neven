import random
n = int(input("-->"))
while True:
  a = ""
  for i in range(random.randint(3, 12)):
    a += random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","C","E","G","I","K","N","P","R","T","V","X","Z"," "," "," "," "," "," ",":",";","\"\"","!","%","[","]","{","}","=","<",">"])
  for i in range(abs(n)):
    b = ""
    while a.rstrip(" ") != b:
      b = input(a + "\n")