t1 = (1, 2, 3, 4, 1, 4, 5)

# 1 is present or not
print(1 in t1)

for item in t1:
    print(item)

for index in range(len(t1)):
    print(t1[index])

# For converting tuple into list
t1 = list(t1)
print(t1)

t1.append(10)

print(t1)

l1 = [1, 2, 3, 4]
t1 = tuple(l1)
print(t1)

s1 = (1, 2, 3, 4)
print(s1[0:3])
print(s1[:2])
print(s1[1:])