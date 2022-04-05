from random import randint
objects = ["rock","paper","scissors"]
winners = [[0,2,1],
           [1,0,2],
           [2,1,0]]

p1 = randint(0,2)
p2 = randint(0,2)
print("Player 1 selects", objects[p1])
print("Player 2 selects", objects[p2])

winner = winners[p1][p2]
if (winner == 0):
    print("It’s a tie")
else:
    print("Player %d wins" % winner)

