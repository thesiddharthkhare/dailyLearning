def solve(N):
    for i in range(N):
        bag = ""
        for j in range(N):
            if i==0 or j==0 or j==N-1:
                bag = bag + "* "
            else:
                bag = bag + "  "
        print(bag)
solve(5)