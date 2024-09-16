def solve(arr, N):
    for i in range(N-1, -1, -1):
        print(arr[i][0], end=" ")
    for j in range(1, N, 1):
        print(arr[0][j], end = " ")
    for i in range(1, N, 1):
        print(arr[i][N-1], end = " ")
    for j in range(N-2, 0, -1):
        print(arr[N-1][j], end = " ")
    print()



a = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]
n = 3

a1 = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12], 
     [13, 14, 15, 16]]
n1 = 4

solve(a, n)
solve(a1, n1)