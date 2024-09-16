# Pattern Printing

# i - start - 1, end - 6
# j - start - 1, end - 11

for i in range(1, 6, 1): #Sir's method
    bag = ""
    for j in range(1, 11, 1):
        bag = bag + "* "
    print(bag)

# My method
print("My method")
for i in range(5):
    for j in range(10):
        print("*", end=" ")
    print()

