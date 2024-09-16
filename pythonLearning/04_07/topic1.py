# Mutability : can change
# Immutability : cannot edit when created

numbers = [1, 2, 3, 4, 5]
numbers[2] = 10
numbers.append(20)
print(numbers)
#list is mutable

# name = "pablo"
# name[1] = "P"
# print(name)
#string data-type is immutable

#Set
# fruits = ["Apple", "Banana", "Tomato", "Apple"]
# print(fruits)
#If we want to print a fruit only one time we use set
# Set - {}

fruits = {"Apple", "Banana", "Tomato", "Apple"}
print(fruits)
#In set, if there is any duplicacy present it will ignore that
# Set is not ordered it is random
#Set does not support indexing
# fruits = {"Apple", "Banana", 1, 1}
# print(fruits[0])

print(len(fruits))
