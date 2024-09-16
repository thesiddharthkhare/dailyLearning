name = "Masai SchOOl"

#skip all the presence of s
# "Maai chool"

bag = ""
# for item in name:
#     if item == "S" or item == "s":
#         continue
#     bag = bag + item

# print(bag)

for item in name:
    if item.lower() == "a" or item.lower() == "e" or item.lower() == "i" or item.lower() == "o" or item.lower() == "u":
        continue
    bag = bag + item
print(bag)   

name = ["pablo", "chunnu", "munnu"]
count = 0
#count of n

for item in name:
    for i in item:
        if i == "n":
            count = count + 1
print(count)            
