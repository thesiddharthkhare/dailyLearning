# MultiDimensional List / 2D array

fields = [
    ["a1", "a2", "a3", "a4"],
    ["a1", "a2f2", "a3", "a4"],
    ["a1", "a2", "a3", "a4"],
    ["a1", "a2", "a3", "a4"]
]

# print(fields)
print(fields[0][1])
print(fields[1][1]) #indexing in multidimensional list


for i in range(4):
    bag = ""
    for j in range(4):
        # print(i, j)
        # print(fields[i][j])
        bag = bag + fields[i][j] + " "
    print(bag)

# print(len(fields))
# print(len(fields[0]))