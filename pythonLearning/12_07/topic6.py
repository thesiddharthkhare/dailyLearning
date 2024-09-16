list = [
    [1, 8, 9],
    [2, 7, 10],
    [3, 6, 11],
    [4, 5, 12]
]

# output : 9 10 11 12 8 7 6 5 1 2 3 4 

# index:
#  (0,0) (0,1) (0,2)
#  (1,0) (1,1) (1,2)
#  (2,0) (2,1) (2,2)
#  (3,0) (3,1) (3,2)

# observation
# j is fixed - reversed
# i is moving - normal flow
# Rule : whatever is fixed that will be our outer loop
# whatever is moving that will be our inner loop

bag = "" # if we want the output in one line
for j in range(len(list[0])-1, -1, -1):
    # bag = " "  # if we want to print after every iteration
    for i in range(len(list)):
            bag = bag + str(list[i][j]) + " "
print(bag)

