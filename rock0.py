from random import randint
objects = ["rock","paper","scissors"]
p1 = objects[randint(0,2)]
p2 = objects[randint(0,2)]
print("Player 1 selects", p1)
print("Player 2 selects", p2)
if (p1 == p2):
    print("It’s a tie")
elif (p1 == "rock") and (p2 == "paper"):
    print("Player 2 wins")
elif (p1 == "rock") and (p2 == "scissors"):
    print("Player 1 wins")
elif (p1 == "paper") and (p2 == "rock"):
    print("Player 1 wins")
elif (p1 == "paper") and (p2 == "scissors"):
    print("Player 2 wins")
elif (p1 == "scissors") and (p2 == "rock"):
    print("Player 2 wins")
elif (p1 == "scissors") and (p2 == "paper"):
    print("Player 1 wins")

