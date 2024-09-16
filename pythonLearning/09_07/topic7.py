# index
# [1, 2, 3, 4]
# index(2) - 1

def my_index(list, num):

    res = -1
    for index in range(len(list)):
        if list[index] == num:
            res = index
            break
    return res



r = my_index([1, 2, 4, 4, 2], 2)
print(r)