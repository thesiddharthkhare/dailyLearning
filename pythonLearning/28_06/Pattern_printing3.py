def solve(N):
    for i in range(N):
        bag =""
        for j in range(N):
            if i == 0 or i == N-1:
                bag = bag + "* "
            else:
                if j == N-1:
                    bag = bag + "* "
                else:
                    bag = bag + "  "
        print(bag)
solve(5)

n = 5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n-1:
            print("*", end= " ")
        else:
            print(" ", end=" ")
    print()