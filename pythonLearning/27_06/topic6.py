for sultan in range(1, 11):
    for bahubali in range(1, 11):
        if sultan < bahubali:
            break
        print(sultan, bahubali)

for i in "ABCD":
    for j in "ABCD":
        if i == j:
            continue
        print(i, j)