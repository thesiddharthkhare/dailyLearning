// Rest and Spread Operators

//Rest Operator
var [firstNo, secondNo,  ...remaining] = [1,2,3,4,5,6,7,8,9]

console.log(firstNo);
console.log(remaining);
console.log(secondNo);

// Spread Operator
// It allows us to expand an array or an object 
// eaach element is passed as a separate argument
var arr = [1, 2, 3, 4, 5];
console.log(...arr);

var arr1 = [7, 8, 9, ...arr];

var arr2 = [7, 8, 9, arr];

console.log(arr1);
console.log(arr2);

var user = {
    batch: "Full Time",
    course: "HTML & CSS"
};

var user1 = {
    ...user,
    name: "Kuldeep",
    age: 23,
};

console.log(user1);