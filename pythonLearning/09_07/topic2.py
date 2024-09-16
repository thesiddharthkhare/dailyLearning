# List inbuilt function

list = [1, 2, 3, 5, 4]
print(len(list))

list.append(20)
list.append(35)
print(list)

l1 = [1, 2, 3, 5, 4]
l2 = [1, 20, 30]

print(l1 + l2)

#insert 35 in index 1
l1.insert(1, 35)
print(l1)

l1.remove(5)
print(l1)

l1.pop      #removes element from the last
print(l1) 

list1 = [10, 3, 5, 3, 24, 31, 6]
list1.sort()  # for ascending order
print(list1)
list1.sort(reverse=True)  #for descending order
print(list1)

