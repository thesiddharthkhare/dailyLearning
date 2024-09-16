sentence = "Masai"

bag = ""
for item in  sentence:
    bag = bag + item

print(bag)

#String 
quote = "Hardwork beats the talent when talent does not work hard"

fruits = "apple,banana,orange,grape"

date = "2024-07-03"
print(quote.split())
print(fruits.split(","))
print(date.split("-"))


# list to string conbversion

s = ["sam", "is", "an", "honest", "person"]

print("".join(s))
print("+".join(s))
print(" ".join(s))

# string to list : use split
# list to string : use join