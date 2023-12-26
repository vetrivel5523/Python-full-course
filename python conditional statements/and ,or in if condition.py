# and using if

a=int(input("enter the a value: "))
b=int(input("enter the b value: "))
c=int(input("enter the c value: "))
if a>b and a>c:
    print("a is big")
    if b>c:
        print("b is big")
    else:
        print("c is big")

# or using if

a=int(input("enter the a value"))
b=int(input("enter the b value"))
c=int(input("enter the c value"))
if a>b or a>c:
    print("a is big")
    if b>c:
        print("b is big")
    else:
        print("c is big")