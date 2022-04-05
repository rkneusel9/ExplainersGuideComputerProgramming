from random import randint
n = int(input("How many flips? "))
heads = 0
tails = 0
for i in range(n):
    if (randint(0,1) == 0):
        heads = heads + 1
    else:
        tails = tails + 1
print("%d heads, %d tails" % (heads, tails))

