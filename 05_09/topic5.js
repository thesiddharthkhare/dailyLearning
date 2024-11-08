//Type Coercion => Implicit Conversion
// 1. String to number
var p  = 6,
    q = '5';

console.log(p - q);
// JS will implicity convert the type for operations

// 2. Number to string
console.log(p + q);

// 3. Boolean to number 
console.log(true + 0);
console.log(false + 0);
// js considers 
// true = 1, false = 0

// 4. Eqq=uality Operation
console.log(p == q);


// Type Conversion => Explicit => Type Casting => done by developes

// 1. Number()
console.log(Number('123'));

// 2. Boolean()
console.log(Boolean(20));
console.log(Boolean(0));
console.log(Boolean(-10));
console.log(Boolean(""));

// 3. parseInt()
console.log(parseInt(124.324));
console.log(parseInt("124"));
console.log(parseInt("124abc"));
console.log(parseInt("abc"));

// 4. parseFloat()
console.log(parseFloat("123"))
console.log(parseFloat("123.45"))
console.log(parseFloat("123.0abc"))
console.log(parseFloat("123.04"))
// 123.0 => 123. => 123
// 123.04 => 123.04

//5. String()
console.log(String(123));
console.log(String(true));