a=int(input("enter the value : "))
if (a%400==0)or(a%100!=0)and(a%4==0):
    print(" given number is leap year")
else:
    print("given number is not leap year")