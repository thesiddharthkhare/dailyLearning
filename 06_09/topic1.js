// Primitive data-types
// numbers, strings, boolean, null, undefined, symbol, bigInt => stored by vlues

// Non-Primitive Data-types
// Objects, Arrays, Functions => stored by reference

var a = 10;
var b = a;
// b is now a copy of a

b = 20;
console.log(a);
console.log(b);

var obj1 = { user: "Arnab"}

var obj2 = obj1;
// obj2 is a reference to abj1
obj2.user = "Tejas"

console.log(obj1.user);
console.log(obj2.user);

var str = "Hello"
var str2 = str
// str2 is a copy of str
str2 = "Welcome"

console.log(str);
console.log(str2);

var arr1 = [1, 2, 3];

var arr2 = arr1;
// arr2 is a reference of arr1

arr2[0] = 4;
console.log(arr1);
console.log(arr2);