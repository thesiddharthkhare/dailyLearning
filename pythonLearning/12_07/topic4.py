m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# find sum of even elements

for i in range(len(m)):
    sum = 0
    for j in range(len(m[0])):
        if m[i][j] % 2 == 0:
            sum += m[i][j]
    print(sum)