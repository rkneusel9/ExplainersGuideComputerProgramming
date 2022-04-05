from math import floor
m = int(input("Month? "))
m = m - 2
if (m==0):
    m = 12
elif (m==-1):
    m = 11
print()
k = int(input("Day of the month? "))
print()
y = int(input("Year? "))
c = y // 100
d = y % 100
w=(floor(2.6 * m-0.2)+k+d+floor(d/4.0)+floor(c/4.0)-2 * c)%7
days = ["Sunday","Monday","Tueday","Wednesday","Thursday",
"Friday","Saturday"]
print(days[w])

