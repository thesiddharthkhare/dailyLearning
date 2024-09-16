var num = 300,
    name = "Masai",
    fullAttendance = true,
    data = {naem: "Pritam"},
    marks = [1,2,3,4]

//check data-type
console.log(typeof num)
console.log(typeof name)
console.log(typeof fullAttendance)
console.log(typeof data)
console.log(typeof marks)

//truthy and falsy

//true, 10

//0, false, null, undefined, NaN, '', "", ``
//NaN => not a number

var declareVar // JS by defalult will assign undefined
console.log(declareVar)
console.log(typeof declareVar)

declareVar = 300
console.log(declareVar)

declareVar = null // null is giev by the user
console.log(declareVar)
console.log(typeof declareVar)


// Mathematical Operators => + - * /

// Modulo Operator => % => remainder
var rem = 5%2
console.log(rem)

// Exponentiation Operator => **
var pw = 2**0.5
console.log(pw)

//Realational Operators => >, >=, <, <=
//Comparison Operators => ==, !=, ===, !==