def find_sum(a, b):
    sum = a + b
    return sum

num = find_sum(26, 10)
print(num)

# Great a user when user login
def great_user(name) :
    print("Hello,", name, "Welcome to the Application")

great_user("Siddharth")    
great_user("Bishal")

#We can pass n number of parameters
#Area of rectangle

def rect_area(h, w):
    print("Area = ", h*w)

rect_area(10, 5)    
rect_area(20, 25)  

#Area of rect + 200
def rect_are(h, w):
    return h * w
    a = 10   #any code after return will not get executed
    b = 20
    print(a * b)

a1 = rect_are(10, 5)
a2 = rect_are(20, 25)
print(a1, a2)
