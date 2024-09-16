# N=4
# for i in range(N, 0, -1):
#     bag = ""
#     for j in range(N, 0, -1):
#         bag = bag + str(j) + " "
#     print(bag)
def solve(N):
    for i in range(N):
        for j in range(N, 0, -1):
            print(j, end=" ")
        print()
solve(5)



