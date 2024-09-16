# OJ problems
char = "abcdefghijklmnopqrstuvwxyz"
N = 26
for num in range(N):
    # print(char[num] + "-" + str(num+1))
    print(char[num], num+1, sep="-")

for num in range(N):
    char = chr(ord('a') + num)
    print(char, num + 1, sep = "-")

def solve(N):

    res = {}
    char = "abcdefghijklmnopqrstuvwxyz"

    for i in range(N):
        res[ char[i]] = i+1

    print(res)
    for item in res:
        print(item, res[item], sep = "-")
solve(26)