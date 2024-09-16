# Inbuilt Function

s = "Hello World"

#o is present or not
print(s.find("o"))
print(s.find("p"))

#replace all the space by a +
print(s.replace(" ", "+"))

# how to find if o is present or not
print(s.index("o"))  #gives the first index where it is present
print(s.rindex("o")) #gives the last index 

#startswith
#endswith
print(s.startswith("Hell")) 
print(s.startswith("hell"))

print(s.endswith("ld"))
print(s.count("o")) #case-sensitive
