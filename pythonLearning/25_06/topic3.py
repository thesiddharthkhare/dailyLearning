# Indentation
# Print avg of numbers from 1 to 100
start = 1
end = 100
sum = 0
count = 0

while start <= end:
    sum += start
    count += 1
    start += 1

avg = sum/count
print(avg) 


#Print the average of all the odd numbers
start = 1
end = 100
count = 0
sum = 0

while start <= end:
    if start % 2 != 0:
        count += 1
        sum += start
    start += 1

print("The sum of odd numbers is ", sum)
print("the average of sum of odd numbers is ", sum/count)
        