var str1 = "Masai"
var str2 = "School"

console.log(str1 + " " + str2)

var name
name = "Pritam"
name = "Kuldeep"

console.log("Hi " + name + ". Welcome back")

// Template Literals => ``

console.log(`Hi ${name}. Welcome back`)

var a = 5,
    b = 6

console.log(`The sum of a and b is ${a+b}`)

var fruit = "apple"
var qty = 5

console.log("You have " + qty + " " + fruit + "s.\n" + "Please come agin")

console.log(`You have ${qty} ${fruit}s.
Please come again`)

//ternary operator => ?
var hasMembership = true
console.log(`The user is ${hasMembership ? `a member` : `not a member`}`)
