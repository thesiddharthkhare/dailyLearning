// Functions
// Declaring/defining a function
function add(a, b){
    var sum = a + b
    // console.log(sum)
    return sum // if not returned we will get undefined
}

//a,b => parameters
//parametres => part of function and once declared, these are constant

// Calling/Executing a function
var addition = add(2, 3)
//2,3 => arguments
//arguments => values provided at the point of function execution and these are constant

console.log(addition)

var addAnother = add(addition, 7)
// if we use return we can perform such operations

function sayHello(){
    console.log("Welcome to the first session of JS")
}
sayHello()