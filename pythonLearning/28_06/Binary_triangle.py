# n = 5
# for i in range(n):
#     for j in range(i+1):
#         if j%2==0:
#             print(1, end="")
#         else:
#             print(0, end="")
#     print()

def solve(N):
    for i in range(1, N+1):
        bag =""
        for j in range(1, i+1):
            if j%2 == 1:
                bag = bag + "1"
            else:
                bag = bag + "0"
        print(bag)
solve(5)