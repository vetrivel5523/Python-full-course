for row in range(15):
    for col in range(30):
        if row in {0} and col in {2,4,6,8,10,12,14,16,18}:
            print("-",end=" ")
        elif row in{0} and col in{0,20}:
            print("|",end=" ")
        elif row in{1} and col in {2,4,6,8,10,12,14,16,18}:
            print("-",end=" ")
        elif row in{1} and col in{0,20}:
            print("|",end=" ")
        elif row in{2} and col in{0,2,25,27}:
            print("|",end=" ")
        elif row in{3} and col in{2,4,6,8,10,12,14,16,18}:
            print("-",end=" ")
        elif row in{3} and col in{0,20}:
            print("|",end=" ")
        elif row in{4} and col in{2,4,6,8,10,12,14,16,18}:
            print("-",end=" ")
        elif row in{4} and col in{0,20}:
            print("|",end=" ")
        elif row in{5} and col in{0,2,6,10,14,18,20}:
            print("|",end=" ")
        elif row in{5} and col in{4}:
            print("7",end=" ")
        elif row in{5} and col in{8}:
            print("8",end=" ")
        elif row in{5} and col in{12}:
            print("9",end=" ")
        elif row in{5} and col in{16}:
            print("+",end=" ")
        elif row in{6} and col in {2,4,6,8,10,12,14,16,18}:
            print("-",end=" ")
        elif row in{6} and col in{0,20}:
            print("|",end=" ")
        elif row in{7} and col in{0,2,6,10,14,18,20}:
            print("|",end=" ")
        elif row in{7} and col in{4}:
            print("4",end=" ")
        elif row in{7} and col in{8}:
            print("5",end=" ")
        elif row in{7} and col in{12}:
            print("6",end=" ")
        elif row in{7} and col in{16}:
            print("-",end=" ")
        elif row in{8} and col in {2,4,6,8,10,12,14,16,18}:
            print("-",end=" ")
        elif row in{8} and col in{0,20}:
            print("|",end=" ")
        elif row in{9} and col in{0,2,6,10,14,18,20}:
            print("|",end=" ")
        elif row in{9} and col in{4}:
            print("1",end=" ")
        elif row in{9} and col in{8}:
            print("2",end=" ") 
        elif row in{9} and col in{12}:
            print("3",end=" ")
        elif row in{9} and col in{16}:
            print("*",end=" ")
        elif row in{10} and col in {2,4,6,8,10,12,14,16,18}:
            print("-",end=" ")
        elif row in{10} and col in{0,20}:
            print("|",end=" ")
        elif row in{11} and col in{0,2,6,10,14,18,20}:
            print("|",end=" ")
        elif row in{11} and col in{4}:
            print(".",end=" ")
        elif row in{11} and col in{8}:
            print("0",end=" ")
        elif row in{11} and col in{12}:
            print("=",end=" ")
        elif row in{11} and col in{16}:
            print("/",end=" ")
        elif row in{12} and col in {2,4,6,8,10,12,14,16,18}:
            print("-",end=" ")
        elif row in{12} and col in{0,20}:
            print("|",end=" ")
        elif row in{13} and col in {2,4,6,8,10,12,14,16,18}:
            print("-",end=" ")
        elif row in{13} and col in{0,20}:
            print("|",end=" ")   
        else:
            print(" ",end="")
    print()
    
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice : ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")

