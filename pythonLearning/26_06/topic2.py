# Continue Statement

total_guest = 7
start_guest = 1
sick_guest = 4

while start_guest <= total_guest:
    if start_guest == 4:
        start_guest += 1
        continue

    print("Guest", start_guest)
    start_guest += 1


"""Print the numbers which are not divisible by
3 or 5 from 1 to 50    """

start = 1
end = 50

while start <= end:
    if start % 5 == 0 or start % 3 == 0:
        start += 1
        continue
    print(start)
    start += 1