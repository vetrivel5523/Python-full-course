#arithmetic operator

a=10
b=2
print(a+b)
print(a**2) #power
print(a//b) #floor division
print(a%b)  #remainder

#assignment operator

a=20
a=a+30
print(a)

#comparision operator

a=10
b=20
c=a>b
print(c)

#logical operator
      # is
      # is not
#is

x=["apple","banana"]
y=["apple","mango"]
z=x
print(x is z)
print(x is y)
print(x==y)

#is not


x=["apple","banana"]
y=["apple","mango"]
z=x
print(x is not z)
print(x is not y)
print(x!=y)

#membership operator
        # in
        # in not

   # in

x=["apple","banana"]
print("banana" in x) #true
print("grape" in x) #false

    # in not

y=["apple","banana"]
print("grape" not in y)  #true
print("apple" not in y)  #false