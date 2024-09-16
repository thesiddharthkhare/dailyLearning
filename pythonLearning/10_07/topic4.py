userName = {
    "first_name" : "Chunnu",
    "last_name" : "Laal",
    "age" : 23,
    "is_student" : True,
    "hobbies" : ["Cricket", "Coding"],
    "city" : "Bangalore",
    "district" : "KA"
}
# How to add a new key
userName["dob"] = "YYYY-MM-DD" 
userName["fav books"] = ["Rich dad poor Dad", "Zero", "Ikigai", "Zero to one"] 

userName["test"] = {
    "a" : "vedfs"
}

userName["dob"] = "2000-12-03" #update the key
print(userName)

# How to check if a key is present or not
print("city" in userName)
print("ci" in userName)