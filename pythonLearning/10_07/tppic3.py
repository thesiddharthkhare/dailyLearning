# How to run a loop in my dictionary
userName = {
    "first_name" : "Chunnu",
    "last_name" : "Laal",
    "age" : 23,
    "is_student" : True,
    "hobbies" : ["Cricket", "Coding"],
    "city" : "Bangalore"
}
for item in userName:
    print(item, userName[item])

print(len(userName))

# How to remove any element dynamically

userName.pop("city")
print(userName)

del userName["age"]
print(userName)

userName.popitem()  #deletes from the last
print(userName)

userName.clear()  # clears all the keys and gives empty dictionary on printing
print(userName)
# as in set we have unique value stored, in dictionary 
# we have unique key stored 
# so suppose age = 27 if assigned,
# the latest updated age will be printed

