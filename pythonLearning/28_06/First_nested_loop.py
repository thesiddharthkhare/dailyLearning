# https://oj.masaischool.com/contest/12430?password=87128 

def print_number_grid(num):
    for i in range(num):
        for j in range(num):
            print(j+1, end=" ")
        print()

print_number_grid(4)

#  Sir method

# def print_number_grid(num):
#     for i in range(num):
#         bag = ""
#         for j in range(1, num+1):
#             bag = bag + str(j) + " "
#         print(bag)

# print_number_grid(4)
