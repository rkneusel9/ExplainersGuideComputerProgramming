from random import randint
n = int(input("How many flips? "))
h = len([i for i in [randint(0,1) for k in range(n)] if i==0])
print("%d heads, %d tails" % (h,n-h))

