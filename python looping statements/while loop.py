i=1
while i<6:
    #print(i)
    #we get horizontal output use print(i,end="")
    print(i,end="")
    i=i+1
print()  # new line
#break

i=1
while i<6:
    print(i,end="")
    if i==3:
        break
    i=i+1
print()

#continue

i=1
while i<6:
    i=i+1
    if i==3:
        continue
    print(i,end="")
print()

#odd in while loop

i=2
while i<11:
    print(i,end="")
    i=i+2
print()


#even in while loop

i=1
while i<11:
    print(i,end="")
    i=i+2
print()