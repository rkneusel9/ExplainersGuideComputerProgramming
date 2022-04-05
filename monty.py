from random import randint

def PlayGame():
    car = randint(0,2)
    guess = randint(0,2)
    if (guess == car):
        return 1,0
    else:
        return 0,1

n = 1000000
winInitial = 0
winChange = 0

for i in range(n):
    a,b = PlayGame()
    winInitial += a
    winChange += b

pinit = 100.0 * winInitial/n
pchange = 100.0 * winChange/n

print("Win, no change: %6.2f%%" % pinit)
print("Win, change doors: %6.2f%%" % pchange)

