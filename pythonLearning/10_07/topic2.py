# Dictionary is a collection of key value pair

student = {
    "name" : "Rahul",
    "age" : 23,
    "location" : "Nainital",
    "is_married" : False,
    "is_student" : True,
    "highest_degree" : "btech"
}
print(student)
print(student["name"])   # how to access location
print(student["is_married"])


# userName = {
#     0 : "Chunnu",
#     1 : "Laal",
#     2 : 23,
#     3 : True,
#     4 : ["Cricket", "Coding"]
# }
# print(userName[1])

userName = {
    "first_name" : "Chunnu",
    "last_name" : "Laal",
    "age" : 23,
    "is_student" : True,
    "hobbies" : ["Cricket", "Coding"]
}
print(userName["hobbies"][0])
# print(userName["city"])

if userName["is_student"]:
    print("I am a masai student and I am working on my skils to get high salary")
else:
    print("I got placed with high slaary")