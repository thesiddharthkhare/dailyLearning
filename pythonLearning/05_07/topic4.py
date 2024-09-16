# Create a fun - store the max vslue

def max_value_from_list(list):

    max = list[0]
    for item in list:
        if item > max:
            max = item
    print(max)        

list = [1, 2, 3, 4, 7, 3, 2]
max_value_from_list(list)

#using return
def max_value_from_list(list):

    max = list[0]
    for item in list:
        if item > max:
            max = item
    return max        

list = [1, 2, 3, 4, 7, 3, 2]
m = max_value_from_list(list)
print(m)

#for min
def min_value_from_list(list):

    min = list[0]
    for item in list:
        if item < min:
            min = item
    print(min)        

list = [1, 2, 3, 4, 7, 3, 2]
min_value_from_list(list)