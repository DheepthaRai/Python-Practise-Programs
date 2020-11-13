z = int(input("Enter a number: "))

def iter(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n%2 != 0):
            return False
        n = n // 2
    return True

if z>0:
    if iter(z):
        print(iter(z))
    else:
        print("False")
else:
    print("Not a positive integer")
