import random

def winGame(compt, player):
    if (compt == player):
        return None
    elif (compt == "r"):
        if (player == "s"):
            return False
        elif (player == "p"):
            return True
    elif (compt == "s"):
        if (player == "p"):
            return False
        elif (player == "r"):
            return True
    elif (compt == "p"):
        if (player == "r"):
            return False
        elif (player == "s"):
            return True


randomNo = random.randint(1, 3)
if (randomNo == 1):
    compt = "r"
elif (randomNo == 2):
    compt = "s"
elif (randomNo == 3):
    compt = "p"


player = input("Your Turn: Rock(r) Paper(p) or Scissers(s): ")
print(compt)

result = winGame(compt, player)
if (result == None):
    print("The Game is Tie!")
elif (result == True):
    print("You Win!")
elif (result == False):
    print("You Loose!")