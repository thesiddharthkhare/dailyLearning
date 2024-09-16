# Function chaininig
str = "helloworld"
l = list(str)
print(l)

l.sort(reverse=True)
str = "".join(l)
print(str)

