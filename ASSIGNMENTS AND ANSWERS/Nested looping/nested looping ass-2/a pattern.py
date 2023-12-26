for row in range(5):
    for col in range(7):
        if row in {0} and col in {3}:
            print("*",end=" ")
        elif row in {1} and col in {2,4}:
            print("*", end=" ")
        elif row in {2} and col in {1,2,3,4,5}:
            print("*", end=" ")
        elif row in {3} and col in {0,6}:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()