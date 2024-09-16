fields = [
    ["a1", "a2", "a3"],
    ["a1", "a2f2", "a3"],
    ["a1", "a2", "a3"],
    ["a1", "a2", "a3"]
]

for i in range(len(fields)):  #row value
    bag = ""
    for j in range(len(fields[0])):  #column value
        bag = bag + fields[i][j] + " "

    print(bag)
