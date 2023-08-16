# Using a `for` loop, print out all odd numbers from 1 to 100.
x = 1
for x in range(1,101):
    if  x%2 != 0:
        print(x)
        x+=1