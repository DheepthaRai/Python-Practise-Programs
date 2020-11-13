import math as m

def Log(x):
    return (m.log10(x) / m.log10(m.sqrt(x)))

def isSquare(n):
    return (m.ceil(Log(n)) == m.floor(Log(n)) == 2)

z = int(input("Enter number: "))

if z>0:
    if isSquare(z):
        if m.sqrt(z) == int(m.sqrt(z)):
            print("True. The given number %s is the square of %s" %((z),int((m.sqrt(z)))))
        else:
            print("False :/")
    else:
        print("False")
else:
    print("Not a positive integer")
