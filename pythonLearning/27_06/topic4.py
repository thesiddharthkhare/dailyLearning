for i in range(1, 6, 1):
    bag = ""
    for j in range(1, i+1):
        bag = bag + str(j) + " "
    print(bag)    

for i in range(5):
    for j in range(i + 1):
        print(j+1, end=" ")
    print()