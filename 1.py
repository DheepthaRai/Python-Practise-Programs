z = int(input("Enter a number: "))

if z>=0:
    if z%2==0:
        if ((z//2)%2)==0:
            print("True :)")
        else:
            print("False :/")
    else:
        print("False")
else:
    print("Not a positive integer")