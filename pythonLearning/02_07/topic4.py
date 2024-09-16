# Operations on list
#Add
brands = []
brands.append("Apple")
brands.append("Oppo")
brands.append("Samsung")
brands.append(10)
print(brands)


#For adding an element at a specific index
# insert
# brands.insert(index, element)

brands.insert(1, "One plus")

brands[2] = "One plus" #re-assigning 

print(brands)

# Remove
nums = [1, 2, 3, 4, 5, True, "Masai"]

nums.pop() #removes the element from last
nums.pop(3) # removes the specific element

#to remove a particular value without knwing its index
nums.remove(5)

print(nums)

