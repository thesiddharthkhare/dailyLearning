m = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for i in range(len(m)):
    bag = ""
    for j in range(len(m[0])):
        bag = bag + str(m[i][j]) + " "
    print(bag)

# to find sum of each row

for i in range(len(m)):
    sum = 0
    for j in range(len(m[0])):
        sum = sum + m[i][j]
    print(sum)

