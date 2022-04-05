from random import random
n = int(input("Number of points? "))
pi = 0
for i in range(n):
    if (random() ** 2+random() ** 2) < 1:
        pi += 1
pi = 4.0 * (pi/n)
print("Estimate of pi is %0.6f" % pi)

