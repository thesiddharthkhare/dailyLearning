def solve(N, M, arr):
    def is_prime(num):
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                count += 1
            if count == 2:
                return True
            return False
    prime_count = 0
    for i in range(N):
        for j in range(M):
            if is_prime(arr[i][j]):
                prime_count += 1
    print(prime_count)
n = 3
m = 3
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
solve(n, m, arr)

