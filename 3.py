import math as m

def Log(x):
    return (m.log10(x) / m.log10(4))

def is4sPower(n):
    return (m.ceil(Log(n)) == m.floor(Log(n)))

z = int(input("Enter number: "))

if z>0:
    if is4sPower(z):
        print("True")
    else:
        print("False")
else:
    print("Not a positive integer")
