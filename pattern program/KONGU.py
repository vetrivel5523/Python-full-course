for row in range(5):
    for col in range(60):
        if row in {0} and col in {0,3}:
            print("K",end=" ")
        elif row in {0} and col in {5,6,7,8}:
            print("O",end=" ")
        elif row in {0} and col in {10,14}:
            print("N", end=" ")
        elif row in {0} and col in {16,17,18,19,20}:
            print("G", end=" ")
        elif row in {0} and col in {22,26}:
            print("U", end=" ")
        elif row in {0} and col in {}:
            print("N", end=" ")
        elif row in {0} and col in {}:
            print("A", end=" ")
        elif row in {0} and col in {}:
            print("D", end=" ")
        elif row in {0} and col in {}:
            print("U", end=" ")
        elif row in {1} and col in {0,2}:
            print("K", end=" ")
        elif row in {1} and col in {5,8}:
            print("O", end=" ")
        elif row in {1} and col in {10,11,14}:
            print("N", end=" ")
        elif row in {1} and col in {16}:
            print("G", end=" ")
        elif row in {1} and col in {22,26}:
            print("U", end=" ")
        elif row in {1} and col in {}:
            print("N", end=" ")
        elif row in {1} and col in {}:
            print("A", end=" ")
        elif row in {1} and col in {}:
            print("D", end=" ")
        elif row in {1} and col in {}:
            print("U", end=" ")
        elif row in {2} and col in {0,1}:
            print("K", end=" ")
        elif row in {2} and col in {5,8}:
            print("O", end=" ")
        elif row in {2} and col in {10,12,14}:
            print("N", end=" ")
        elif row in {2} and col in {16,18,19,20}:
            print("G", end=" ")
        elif row in {2} and col in {22,26}:
            print("U", end=" ")
        elif row in {2} and col in {}:
            print("N", end=" ")
        elif row in {2} and col in {}:
            print("A", end=" ")
        elif row in {2} and col in {}:
            print("D", end=" ")
        elif row in {2} and col in {}:
            print("U", end=" ")
        elif row in {3} and col in {0,2}:
            print("K", end=" ")
        elif row in {3} and col in {5,8}:
            print("O", end=" ")
        elif row in {3} and col in {10,13,14}:
            print("N", end=" ")
        elif row in {3} and col in {16,18,20}:
            print("G", end=" ")
        elif row in {3} and col in {22,26}:
            print("U", end=" ")
        elif row in {3} and col in {}:
            print("N", end=" ")
        elif row in {3} and col in {}:
            print("A", end=" ")
        elif row in {3} and col in {}:
            print("D", end=" ")
        elif row in {3} and col in {}:
            print("U", end=" ")
        elif row in {4} and col in {0,3}:
            print("K", end=" ")
        elif row in {4} and col in {5,6,7,8}:
            print("O", end=" ")
        elif row in {4} and col in {10,14}:
            print("N", end=" ")
        elif row in {4} and col in {16,17,18,20}:
            print("G", end=" ")
        elif row in {4} and col in {22,23,24,25,26}:
            print("U", end=" ")
        elif row in {4} and col in {}:
            print("N", end=" ")
        elif row in {4} and col in {}:
            print("A", end=" ")
        elif row in {4} and col in {}:
            print("D", end=" ")
        elif row in {4} and col in {}:
            print("U", end=" ")
        else:
            print(" ",end=" ")
    print()