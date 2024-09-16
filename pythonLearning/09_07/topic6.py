# join

# take a list -> string


def my_join(list, basis):
    bag = ""
    for index in range(len(list)):
        if index == len(list) - 1:
            bag = bag + list[index]

        else:   
            bag = bag + list[index] + basis

    return bag


list = ["Hello" , "world", "This", "is", "Masai", "School"]

basis = "+"

res = my_join(list, basis)
print(res)