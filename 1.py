#I have made some sort of a logical error in this and am currently trying to work it out. So it's under progress... Feel free to check it out and may be find the key part I'm missing out on, if you want to :)

z = int(input("Enter a number: "))

def iter(z):
    c = True
    i = 0
    while (z%2)!=0:
        z=z//2
        if z==int(z) and z%2==0:
            i=i+1
            iter(z)
        elif z!=int(z) or z%2!=0:
            c = False
        elif z/2==1:
            c = True
        else:
            c = False
    if c == True and i%2==0:
        return True
    else:
        return False

if z>=0:
    if z%2==0:
        print(iter(z))
    else:
        print("False")
else:
    print("Not a positive integer")
