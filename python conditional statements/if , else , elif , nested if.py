# if

a=100
b=20
if(a>b):
    print("a is big")

# else

a = 10
b = 20
if (a > b):
    print("a is big")
else:
    print("b is big")

# elif

a = 20
b = 20
if (a > b):
    print("a is big")
elif a==b:
    print("a is equal to b ")
else:
    print("b is big")


# nested if (and,or)

a,b,c=10,2,1.5
if(a>b and a>c):
    print("a is big")
    if b>c:
        print("b is big")
    else:
        print("c is big")

# or

a,b,c=10,2,5
if(a>b or a>c):
    print("a is big")
    if b>c:
        print("b is big")
    else:
        print("c is big")


