from random import randint
n = int(input("How many flips? "))
flips = [randint(0,1) for i in range(n)]
heads = len([i for i in flips if i==0])
tails = n - heads
print("%d heads, %d tails" % (heads, tails))

