m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print in a zig-zag pattern
# logic : for odd start to end, but for even end to start

# My method
for i in range(len(m)):
    if i % 2 == 0:
        for j in range(len(m[0])-1, -1, -1):
            print(m[i][j], end = " ")
        print()
    elif i % 2!= 0:
        for j in range(len(m[i])):
            print(m[i][j], end = " ")
        print()


# Sir method
for i in range(len(m)):
    bag = ""
    if i % 2 == 0:
        for j in range(len(m[0])-1, -1, -1):
            bag = bag + str(m[i][j]) + " "
    elif i % 2!= 0:
        for j in range(len(m[i])):
            bag = bag + str(m[i][j]) + " "
    print(bag)
