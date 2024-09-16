# Map characters again
N = 30
# for i in range(26):
#     char = chr(ord("a") + i)
#     print(char, N+i, sep="-")

dict = {}

for i in range(26):
    key = chr(ord("a") + i)
    value = N+i
    dict[key] = value

for key in dict:
    print(key, dict[key], sep="-")

