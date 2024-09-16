# String - reverse

def reverse_string(str):
    bag = ""
    for item in reversed(str):
        bag = bag + item
    return bag

reverse = reverse_string("Pablo")
r2 = reverse_string("Piyush")
print(reverse)    
print(r2)

def check_admin(str):
    if str == "Pablo":
        return "You are admin"
    else:
        return "You are not admin"
    
a1 = check_admin("Pablo")    
a2 = check_admin("Piyush") 
print(a1)   
print(a2)   