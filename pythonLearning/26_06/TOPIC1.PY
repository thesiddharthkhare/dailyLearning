# break statement

total_guest = 7
start_guest = 1

while start_guest <= total_guest:
    if start_guest == 4:
        break

    print("Guest", start_guest)
    start_guest += 1

"""Give the first number which is divisible by 
3 between 50 to 70"""

start = 50
end = 70
while start <= end:
    if start % 3 == 0:
        print(start)
        break
    start += 1 