def N_traversal(N, matrix):
    for j in range(N):
        for i in range(N-1, -1, -1):
            if j==0 or j==i or j==N-1:
                print(matrix[i][j], end=" ")

N =4
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

N_traversal(N, matrix)
