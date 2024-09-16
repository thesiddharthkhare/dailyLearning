def print_diagonals(matrix, r, c, k):
    a = 0
    b = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == k:
                a = i
                b = j
    for i in range(r):
        for j in range(c):
            if i-j == a-b:
                print(matrix[i][j], end=" ")
            if i + j == a + b:
                print(matrix[i][j], end=" ")
    
r = 3
c = 3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 6

print_diagonals(matrix, r, c, k)