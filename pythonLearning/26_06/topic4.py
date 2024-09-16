# Print from 10 to 1

for item in range(10, 0, -1):
    print(item)

# Sum of all numbers btween 1 to 10
sum = 0
for item in range(1, 11):
    sum += item
print(sum)    # For final ans id return inside for, it will give after every iteration

bag = ""
for item in range(1, 11, 1):
    bag = bag + str(item) + " "

print(bag)    


for item in range(1, 11):
    print(item, end=" ")


# Create a program to calculate factorial of a number
num = 3
factorial_result = 1
for item in range(1, num + 1, 1):
    factorial_result *= item

print(factorial_result)    

#Break and continue
total_guest = 7

for item in range(1, total_guest + 1, 1):
    if item == 4:
        break
    print("Guest", item)


for item in range(1, total_guest + 1, 1):
    if item == 4:
        continue #increment/decrement is automatically handle by the for loop
    print("Guest", item)