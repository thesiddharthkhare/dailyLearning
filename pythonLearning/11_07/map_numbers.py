N = 5
K = 10

# for i in range(N):
#     print(i+1, K+i, sep="-")

dict = {}
for i in range(N):
    key = i+1
    value = K+i
    dict[key] = value

for key in dict:
    print(key, dict[key], sep="-")