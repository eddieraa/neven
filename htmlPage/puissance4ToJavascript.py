import random

winPossibility = [
  [(0, 0), (1, 1), (2, 2), (3, 3)], 
  [(1, 1), (2, 2), (3, 3), (4, 4)], 
  [(2, 2), (3, 3), (4, 4), (5, 5)], 
  [(0, 1), (1, 2), (2, 3), (3, 4)], 
  [(1, 2), (2, 3), (3, 4), (4, 5)], 
  [(2, 3), (3, 4), (4, 5), (5, 6)], 
  [(0, 2), (1, 3), (2, 4), (3, 5)], 
  [(1, 3), (2, 4), (3, 5), (4, 6)], 
  [(0, 3), (1, 4), (2, 5), (3, 6)], 
  [(0, 4), (1, 5), (2, 6), (3, 5)], 
  [(1, 5), (2, 6), (3, 5), (4, 4)], 
  [(2, 6), (3, 5), (4, 4), (5, 3)], 
  [(0, 5), (1, 6), (2, 5), (3, 4)], 
  [(1, 6), (2, 5), (3, 4), (4, 3)], 
  [(2, 5), (3, 4), (4, 3), (5, 2)], 
  [(0, 6), (1, 5), (2, 4), (3, 3)], 
  [(1, 5), (2, 4), (3, 3), (4, 2)], 
  [(2, 4), (3, 3), (4, 2), (5, 1)], 
  [(0, 0), (0, 1), (0, 2), (0, 3)], 
  [(0, 0), (1, 0), (2, 0), (3, 0)], 
  [(0, 1), (0, 2), (0, 3), (0, 4)], 
  [(0, 1), (1, 1), (2, 1), (3, 1)], 
  [(0, 2), (0, 3), (0, 4), (0, 5)], 
  [(0, 2), (1, 2), (2, 2), (3, 2)], 
  [(0, 3), (0, 4), (0, 5), (0, 6)], 
  [(0, 3), (1, 3), (2, 3), (3, 3)], 
  [(1, 0), (1, 1), (1, 2), (1, 3)], 
  [(1, 0), (2, 0), (3, 0), (4, 0)], 
  [(1, 1), (1, 2), (1, 3), (1, 4)], 
  [(1, 1), (2, 1), (3, 1), (4, 1)], 
  [(1, 2), (1, 3), (1, 4), (1, 5)], 
  [(1, 2), (2, 2), (3, 2), (4, 2)], 
  [(1, 3), (1, 4), (1, 5), (1, 6)], 
  [(1, 3), (2, 3), (3, 3), (4, 3)], 
  [(2, 0), (2, 1), (2, 2), (2, 3)], 
  [(2, 0), (3, 0), (4, 0), (5, 0)], 
  [(2, 1), (2, 2), (2, 3), (2, 4)], 
  [(2, 1), (3, 1), (4, 1), (5, 1)], 
  [(2, 2), (2, 3), (2, 4), (2, 5)], 
  [(2, 2), (3, 2), (4, 2), (5, 2)], 
  [(2, 3), (2, 4), (2, 5), (2, 6)], 
  [(2, 3), (3, 3), (4, 3), (5, 3)], 
  [(3, 0), (3, 1), (3, 2), (3, 3)], 
  [(3, 1), (3, 2), (3, 3), (3, 4)], 
  [(3, 2), (3, 3), (3, 4), (3, 5)], 
  [(3, 3), (3, 4), (3, 5), (3, 6)], 
  [(4, 0), (4, 1), (4, 2), (4, 3)], 
  [(4, 1), (4, 2), (4, 3), (4, 4)], 
  [(4, 2), (4, 3), (4, 4), (4, 5)], 
  [(4, 3), (4, 4), (4, 5), (4, 6)], 
  [(5, 0), (5, 1), (5, 2), (5, 3)], 
  [(5, 1), (5, 2), (5, 3), (5, 4)], 
  [(5, 2), (5, 3), (5, 4), (5, 5)], 
  [(5, 3), (5, 4), (5, 5), (5, 6)], 
  [(0, 4), (1, 4), (2, 4), (3, 4)], 
  [(0, 5), (1, 5), (2, 5), (3, 5)], 
  [(0, 6), (1, 6), (2, 6), (3, 6)], 
  [(1, 4), (2, 4), (3, 4), (4, 4)], 
  [(1, 5), (2, 5), (3, 5), (4, 5)], 
  [(1, 6), (2, 6), (3, 6), (4, 6)], 
  [(2, 4), (3, 4), (4, 4), (5, 4)], 
  [(2, 5), (3, 5), (4, 5), (5, 5)], 
  [(2, 6), (3, 6), (4, 6), (5, 6)], 
  [(1, 0), (2, 1), (3, 2), (4, 3)], 
  [(2, 1), (3, 2), (4, 3), (5, 4)], 
  [(2, 0), (3, 1), (4, 2), (5, 3)], 
  [(1, 6), (2, 5), (3, 4), (4, 3)], 
  [(2, 5), (3, 4), (4, 3), (5, 3)], 
  [(2, 6), (3, 5), (4, 4), (5, 3)]
]

grille = {}
while True:
  symbol1 = "-"
  symbol2 = "X"
  playerSymbol, computerSymbol = symbol1, symbol2
  symbolTurn = random.choice([symbol1, symbol2])
  for y in range(6):
    for x in range(7):
      grille[y, x] = " "
  
  print("! ! ! ! ! ! ! !\n" * 5 + "!1!2!3!4!5!6!7!")
  mdj = ""
  while mdj not in ["p", "c", "e"]:
    mdj = input("p/c/e ? : ")

  if mdj == "e":
    break

  while True:
    tie = True
    for i in winPossibility:
      result = ""
      for j in i:
        result += grille[j]
      if result.count(" ") != 0:
        tie = False
      for k in [playerSymbol, computerSymbol]:
        if result.count(k) == 4:
          winner = k
          break
        elif result.count(k) == 3 and mdj == "c":
          if result == k * 3 + " ":
            if i[3][0] == 5 or grille[i[3][0] + 1, i[3][1]] != " ":
              IA = i[3][1] + 1
          elif result == k * 2 + " " + k:
            if i[2][0] == 5 or grille[i[2][0] + 1, i[2][1]] != " ":
              IA = i[2][1] + 1
          elif result == k * 1 + " " + k * 2:
            if i[1][0] == 5 or grille[i[1][0] + 1, i[1][1]] != " ":
              IA = i[1][1] + 1
          elif result == " " + k * 3 :
            if i[0][0] == 5 or grille[i[0][0] + 1, i[0][1]] != " ":
              IA = i[0][1] + 1
    
    if "winner" in locals():
      if mdj == "p":
        print("Winner :", winner)
      elif winner == playerSymbol:
        print("Winner : player")
      else:
        print("Winner : calculator")

      toPrint = []
      for y in range(6):
        toPrint.append("")
        for x in range(7):
          toPrint[-1] += "!" + grille[y, x]#.replace(symbol1 if winner == symbol2 else symbol2, ";")
        toPrint[-1] += "!"
      print(*toPrint + ["\n"], sep = "\n")

      del winner
      break
    elif tie == True:
      print("Tie")
      break
    
    while True:
      if symbolTurn != computerSymbol or mdj == "p":
        play = input("Joueur " + symbolTurn + " : ")
      else:
        print("IA" in locals())
        if "IA" in locals():
          play = str(IA)
          del IA
        else:
          while grille[0, int(play := str(random.randint(1, 7))) - 1] != " ":pass

        print("Calculatrice :", play)

      if play == "e":
        raise Exception("End")
      
      if play in ["1", "2", "3", "4","5", "6", "7"]:
        if grille[0, int(play) - 1] == " ":
          for i in [5, 4, 3, 2, 1, 0]:
            if grille[i, int(play) - 1] == " ":
              grille[i, int(play) - 1] = symbolTurn
              break
          break

    toPrint=[]
    for y in range(6):
      toPrint.append("")
      for x in range(7):
        toPrint[-1] += "!"+grille[y,x]
      toPrint[-1] += "!"

    print(*toPrint + ["!1!2!3!4!5!6!7!"], sep = "\n")
    
    symbolTurn = symbol1 if symbolTurn == symbol2 else symbol2
  
    """for y in range(6):
      for x in range(7):
        print("!" + str((y,x)), end = "")
      print("!")"""