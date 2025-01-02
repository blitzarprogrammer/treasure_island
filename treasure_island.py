print('''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
_''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
crossroad = input("You are at a cross road.\nChoose to go right or left?")
if crossroad == "right":
    print("You fall into a hole.\nGame Over!")
elif crossroad == "left":
    lake = input("You are at a lake and there is an island in the middle of the lake.\nDo you wish to swim or wait for a boat?")
    if lake == "swim":
        print("You are attacked by trout.\nGame Over!")
    else:
        print("You arrived at the island unharmed.There is a house with three doors.")
        unharmed = input("Red one, blue one and yellow one. Which one do you choose?")
if unharmed == "red":
            print("You are burned by fire.\nGame Over!")
elif unharmed == "blue":
                print("You are eaten by beasts.\nGame Over!")
elif unharmed == "yellow":
                print("You won.\nYou are officially the winner.") 
        