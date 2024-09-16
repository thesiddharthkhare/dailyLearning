# Dictionary in Python

l = ["Chunnu", "Laal", 23, True, ["Cricket", "Coding"]]
# first_name, last_name, age, is_student, hobbies

# How to create a dictionary
# key : value

userName = {
    "first_name" : "Chunnu",
    "last_name" : "Laal",
    "age" : 23,
    "is_student" : True,
    "hobbies" : ["Cricket", "Coding"]
}

print(userName)

product_detail = {
    "name" : "MacBook Air",
    "brand" : "Apple",
    "price" : 95000,
    "category" : "Electronics",
    "specification" : {
        "ram" : 8,
        "processor" : "M1",
        "display" : "Apple Retina Display",
        "storage" : 256
    },
    "ratings" : [4.5, 5, 3, 3.5]
}
print(product_detail)

student = {
    "name" : "Rahul",
    "age" : 23,
    "location" : "Nainital",
    "is_married" : False,
    "is_student" : True,
    "highest_degree" : "btech"
}
print(type(student))

students = {
    "student1" : {"name" : "Akhil", "age" : 27},
    "student2" : {"name" : "Ram", "age" : 24}
}