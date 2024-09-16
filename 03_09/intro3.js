//Boolean => true and false
var hasLoggedIn = true

var sym = Symbol("hello")

// Non-primitive data-types - Objects, Array, Function

// [] empty, initialising an array
var marks = [67, 98, 70, 45, 23]
var data = ["Shiv", 23, true, "Bangalore"]

var dataObject = {
    name : "Shiv",
    age : 23,
    hasDrivingLicense : true,
    city : "Bangalore"
} // object - {}
// name,age, hasDrivingLicense, city => keys
// "Shiv", 23, true, "Bangalore" => Values
console.log(data)
console.log(marks)
console.log(marks[1]) 
console.log(dataObject)

// 2 notations => Dot notation and Bracket notation
// Dot Notation
console.log(dataObject.name)

// Bracket Notation
console.log(dataObject["city"])// pass it as a string