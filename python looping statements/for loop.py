#string in for loop

a="orange"
for i in a:
    print(i,end="")
print()

#list in for loop

a=["apple","orange","mango"]
for i in a:
    print(i,end=" ")
print()

#range in for loop

for i in range(1,5):
    print(i,end="")
print()

#dict in for loop

a={"name":"vetrivel","reg no":1}
for i in a:
    print(i,end=",")
print()

#skipping in for loop

for i in range(2,11,2):
    print(i,end=" ")
print()

#muliplication tables
for i in range(1,11):
    print(i,"*",2,"=",i*2)
print()

#factorial program

fact=1
n=int(input("enter the value :"))
for i in range(i,n+i):
    fact=fact*i
    print("fact is ",n,"is",fact)
print()

#prime number

count=0
n=int(input("enter the number :"))
for i in range(i,n+i):
    if n%1==0:
        count=count+1
    if count==2:
        print(n,"prime")
    else:
        print(n,"not prime")

