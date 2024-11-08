// Function Parameters
//strict 

function checkIp(input) {
    if (typeof input === 'string') {
        return input.toUpperCase();
    } else if (typeof input === "number") {
        return input * 2;
    }
    return input;
} 

// Statement vs Expression 

//Statement:
// 1. Perform actions => Execute a specifix action 
// 2. No return values

// Variable declaration
var w = 10;

// Control Flow Statements
if (x > 5) {
    console.log("x is greater than 5");
}

// Expression
// Expressions can be part of statements
// 1. Produces values 
// 2. Can be nested => can be part of statements or larger expressions
// 3. Can be assigned => these produced values can be assigned 

var z = 2 + 3;

var isTrue = (5 > 4) && (6 < 7);
// Mathematical expression

// Statements vs Expressions
// 1. Return values =>
// Statements => do not produce any return values
// Expressions => Always return values 

// 2. Purpose =>
// Statements => execute an action 
// Expression => compute and produce values

