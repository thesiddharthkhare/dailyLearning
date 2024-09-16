# how to put arrays in input

values = (input("Enter your values here").split())

print("Values :", values)

# to convert string values into int 

i = 0
while i < len(values):
    values[i] = int(values[i])
    i += 1
print("Values :", values)

# Another way
print("Please write prices of every item")
prices = list(map(int,(input("Enter your values here :").split())))

# find sum of all prices

total = sum(prices)
print("Total bill is :", total,"Rs")