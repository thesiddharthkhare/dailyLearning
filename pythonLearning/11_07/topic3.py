# get method  - to get any specific value

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

print(classDetails.get("topic"))
print(classDetails["topic"])

print(classDetails.get("test", "This key is not present"))
