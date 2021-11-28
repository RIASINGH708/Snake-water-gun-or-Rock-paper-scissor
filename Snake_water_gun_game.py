#Snake water gun or Rock paper scissor
import random

def gameWin(comp,you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None
    elif comp=='s': #All possibilities when  comp is snake
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':#All possibilities when  comp is water
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':#All possibilities when comp is gun
        if you=='s':
            return True
        elif you=='w':
            return False



print("Comp turn:Snake(s) Water(w) or Gun(g)?")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

you = input("Your turn:Snake(s) Water(w) or Gun(g)? ")
a=gameWin(comp , you)

print(f"Computer chose {comp}")
print(f"You chose {you}")


if a == None:
    print("The game is tie")
elif a:
        print("You win")
else:
    print("You lose")



