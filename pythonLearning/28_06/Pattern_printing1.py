def solve(N):
    for i in range(N):
        for j in range(N):
            if i==0 or i==N-1 or j==0:
                print("*", end = " ")
        print()

solve(5)

# def solve(N):
#     for i in range(N):
#         bag = ""
#         for j in range(N):
#             if i==0 or i==N-1:
#                 bag = bag + "* "
#             else :
#                 bag = bag + "*"
#                 break
#         print(bag)

# solve(5)
