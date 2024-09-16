def solve(N):
    for i in range(N):
        for j in range(i+1):
            print("*", end="")
        print()

solve(4)

# def solve(N):
#     for i in range(N):
#         bag=""
#         for j in range(i+1):
#             bag = bag + "*"
#         print(bag)
# solve(4)