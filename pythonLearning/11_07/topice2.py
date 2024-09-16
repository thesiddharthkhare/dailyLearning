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

print(list(classDetails.values())[3].values())

inner_dict = classDetails["course_details"]

value = inner_dict.values()

l = list(value)

print(l[1])