start = 1
end = 5

bag = ""

while start <= end:
    bag = bag + "* "
    # print(bag, end="") #If want to print all the * in one line
    print(bag)
    start += 1


# Multiplication table 
table_of = 19    
start = 1
end = 10

while start <= end:
    print(table_of, "*" , start , "=", start * table_of)
    start += 1