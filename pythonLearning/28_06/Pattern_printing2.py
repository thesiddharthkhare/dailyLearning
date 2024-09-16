def solve(N):
    for i in range(N):
        for j in range(N):
            if i == N-1:
                print("*", end= " ")
            elif j==0 or j==N-1:
                print("*", end = " ")
            else:
                print(" ", end=" ")
        print()
                
solve(5)

# def solve(N):
#     for i in range(N):
#         bag = ""
#         for j in range(N):
#             if i==N-1:
#                 bag = bag + "* "
#             else:
#                 if j==0 or j==N-1:
#                     bag = bag + "* "
#                 else:
#                     bag = bag + "  "
#         print(bag)
# solve(5)