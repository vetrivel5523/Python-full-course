for row in range(5):
    for col in range(57):
        if row in {0} and col in {0,8,10,11,12,13,15,16,17,18,19,21,22,23,24,25,26,28,29,30,31,32,33,34,36,44,46,47,48,49,51}:
            print("@", end=" ")
        elif row in {1} and col in {1,7,10,17,21,26,31,37,43,46,51}:
            print("@", end=" ")
        elif row in {2} and col in {2,6,10,11,12,13,17,21,22,23,24,25,26,31,38,42,46,47,48,49,51}:
            print("@", end=" ")
        elif row in {3} and col in {3,5,10,17,21,23,31,39,41,46,51}:
            print("@", end=" ")
        elif row in {4} and col in {4,10,11,12,13,17,21,24,25,26,28,29,30,31,32,33,34,40,46,47,48,49,51,52,53,54,55,56,57}:
            print("@", end=" ")
        else:
            print(" ", end=" ")
    print()
