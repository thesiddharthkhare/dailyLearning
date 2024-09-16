#print numbers from 100 to 1 decrement loop / reverse loop

# start = 100
# while start >= 1:
#     print(start)
#     start = start - 1


# Print sum of all the numbers starting 1 to 100
sum = 0
start = 1
end = 100
while start <= end:
    sum = sum + start #if we want sum at every increment we will print sum here
    start = start + 1
print("The sum is :", sum) # because we want the final ans        


# Count of even numbers from 1 to 10
start = 1
end = 10
count = 0

while start <= end:
    if start % 2 == 0:
        count += 1
    start += 1    

print("Count of even nos is",count)