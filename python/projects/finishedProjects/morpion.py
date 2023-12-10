from math import *
from random import *

print("7!8!9\n4!5!6\n1!2!3")

while (gamemode := input("p/o/e : ")) in ["p", "o"]:
  playerSymbol = choice(["X", "O"])
  botSymbol = "X" if playerSymbol == "O" else "O"
  turnSymbol = choice(["X", "O"])

  grille = {}
  for i in range(9):
    grille[i + 1] = " "

  while True:
    winPossibility = [
      grille[1] + grille[2] + grille[3],
      grille[4] + grille[5] + grille[6],
      grille[7] + grille[8] + grille[9],
      grille[1] + grille[4] + grille[7],
      grille[2] + grille[5] + grille[8],
      grille[3] + grille[6] + grille[9],
      grille[1] + grille[5] + grille[9],
      grille[7] + grille[5] + grille[3]
    ]
    for i in ["X", "O"]:
      if i*3 in winPossibility:
        if gamemode == "p":
          print("Victoire joueur " + i)
        elif playerSymbol == i:
          print("Victoire joueur")
        else:
          print("Victoire ordinateur")
        winner=True

    if "winner" in locals():
      del winner
      break

    if sum([i.count(" ") for i in winPossibility]) == 0:
      print("Egalite")
      break
    
    if gamemode == "p" or playerSymbol == turnSymbol:
      play = input("Joueur " + turnSymbol + ": ")
    else:
      if grille[5] == " ":
        play = 5

      elif winPossibility[0] in [" " + playerSymbol + playerSymbol, " " + botSymbol + botSymbol]:  play = 1
      elif winPossibility[0] in [playerSymbol + " " + playerSymbol, botSymbol + " " + botSymbol]:  play = 2
      elif winPossibility[0] in [playerSymbol + playerSymbol + " ", botSymbol + botSymbol + " "]:  play = 3
      elif winPossibility[1] in [" " + playerSymbol + playerSymbol, " " + botSymbol + botSymbol]:  play = 4
      elif winPossibility[1] in [playerSymbol + " " + playerSymbol, botSymbol + " " + botSymbol]:  play = 5
      elif winPossibility[1] in [playerSymbol + playerSymbol + " ", botSymbol + botSymbol + " "]:  play = 6
      elif winPossibility[2] in [" " + playerSymbol + playerSymbol, " " + botSymbol + botSymbol]:  play = 7
      elif winPossibility[2] in [playerSymbol + " " + playerSymbol, botSymbol + " " + botSymbol]:  play = 8
      elif winPossibility[2] in [playerSymbol + playerSymbol + " ", botSymbol + botSymbol + " "]:  play = 9
      elif winPossibility[3] in [" " + playerSymbol + playerSymbol, " " + botSymbol + botSymbol]:  play = 1
      elif winPossibility[3] in [playerSymbol + " " + playerSymbol, botSymbol + " " + botSymbol]:  play = 4
      elif winPossibility[3] in [playerSymbol + playerSymbol + " ", botSymbol + botSymbol + " "]:  play = 7
      elif winPossibility[4] in [" " + playerSymbol + playerSymbol, " " + botSymbol + botSymbol]:  play = 2
      elif winPossibility[4] in [playerSymbol + " " + playerSymbol, botSymbol + " " + botSymbol]:  play = 5
      elif winPossibility[4] in [playerSymbol + playerSymbol + " ", botSymbol + botSymbol + " "]:  play = 8
      elif winPossibility[5] in [" " + playerSymbol + playerSymbol, " " + botSymbol + botSymbol]:  play = 3
      elif winPossibility[5] in [playerSymbol + " " + playerSymbol, botSymbol + " " + botSymbol]:  play = 6
      elif winPossibility[5] in [playerSymbol + playerSymbol + " ", botSymbol + botSymbol + " "]:  play = 9
      elif winPossibility[6] in [" " + playerSymbol + playerSymbol, " " + botSymbol + botSymbol]:  play = 1
      elif winPossibility[6] in [playerSymbol + " " + playerSymbol, botSymbol + " " + botSymbol]:  play = 5
      elif winPossibility[6] in [playerSymbol + playerSymbol + " ", botSymbol + botSymbol + " "]:  play = 9
      elif winPossibility[7] in [" " + playerSymbol + playerSymbol, " " + botSymbol + botSymbol]:  play = 7
      elif winPossibility[7] in [playerSymbol + " " + playerSymbol, botSymbol + " " + botSymbol]:  play = 5
      elif winPossibility[7] in [playerSymbol + playerSymbol + " ", botSymbol + botSymbol + " "]:  play = 3

      else:play = randint(1, 9)

      print("Ordinteur : " + str(play))

    
    if str(play) in [str(i) for i in range (1,10)] and grille[int(play)] == " ":
      grille[int(play)] = turnSymbol
      turnSymbol = "X" if turnSymbol == "O" else "O"
    print(*[grille[7] + "!" + grille[8] + "!" + grille[9], grille[4] + "!" + grille[5] + "!" + grille[6], grille[1] + "!" + grille[2] + "!" + grille[3]], sep = "\n")