# Session details

classDetails= {
    "topic" : "Dictionary 2",
    "start_time" : "16:30",
    "end_time" : "18:00",
    "course_details" : {
        "batch" : "ft37",
        "course" : "pr104"
    },
    "zoom_link" : "https://zoom.in/y776872532653"
}
#keys
#values
#get
#items
# print(classDetails.keys())  #gives all the keys and gives only parent keys
# print(classDetails.keys()[2])  #gives error because it does not have any index
# print(list(classDetails.keys()))  # coverts into list/ typecasting

keys = list(classDetails.keys())
print(keys[2])

keys1 = classDetails["course_details"]
print(keys1)

print(list(keys1.keys())[1])

print(classDetails.values())
print(list(classDetails.values())) #typecasting
print(list(classDetails.values())[3]["batch"]) #typecasting