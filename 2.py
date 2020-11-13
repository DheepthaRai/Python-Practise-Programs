z = input("Enter a number: ")

def iter(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n%3 != 0):
            return False
        n = n // 3
    return True

if z == int(z) and z>0:
    if iter(z):
        print(iter(z))
    else:
        print("False")
else:
    print("Not a positive integer")
