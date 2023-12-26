x=int(input("enter the value x : "))
y=int(input("enter the value y : "))
big = lambda x, y: print("a is big") if x > y else print("b is big")
print(big(x,y))
