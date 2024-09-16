set1 = {1, 2, 3, "Masai"}
set2 = {3, 4, 6}

#Union - symbol | - pipe
print("Union", set1 | set2)
print("Intersection", set1 & set2) #Intersection & symbol

#Check if element 3 is present or not? 
#To check we use in operator

print(3 in set1)
print(5 in set1)
print(5 not in set1)  #Alternative
print("Masai" in set1)  
print("Masai " in set1)  

#iterate
for item in set1:
    print(item)             

set1 = list(set1) #Converting set into list
set1.append("Test")
set1.append(1)
print(set1)

list1 = [1, 2, 3, "Masai"]

list1 = set(list1) #Converting list into set
print(list1)