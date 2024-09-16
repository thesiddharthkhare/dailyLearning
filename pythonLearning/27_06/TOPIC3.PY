for i in range(1, 6, 1):
    bag = ""
    for j in range(1, i+1):
        bag = bag + "* "
    print(bag)

# My method
print("my method")
for i in range(5):
    for j in range(i+1):
        print("* ", end="")
    print()    