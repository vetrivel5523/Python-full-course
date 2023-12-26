for row in range(5):
    for col in range(7):
        if row in {0} and col in {0,3}:
            print("*",end=" ")
        elif row in {1} and col in {0,2}:
            print("*", end=" ")
        elif row in {2} and col in {0,1}:
            print("*", end=" ")
        elif row in {3} and col in {0,2}:
            print("*", end=" ")
        elif row in {4} and col in {0,3}:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()