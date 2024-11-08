var arr = [1, 2, 3, 4]
console.log(arr);

arr.push(7);
console.log(arr);

arr.pop();
console.log(arr);

arr.unshift(0);
console.log(arr);

arr.shift();
console.log(arr);

var arr1 = [1, 2, 3];
var arr2 = [6, 7, 8];
console.log(arr1.concat(arr2));

console.log(arr.reverse());  // reverse he elements

var Arr = [2,3,9,5,4];
Arr.sort();
console.log(Arr);

var Arr = [2, 3, 9, 5, 14]
Arr.sort(); // by default sort considers them as strings
console.log(Arr);

var str = ['a', 'c', 'd', 'b'];
str.sort();
console.log(str)

var str = ['ab', 'aa', 'ac', 'a']
str.sort();
console.log(str);

var Arr= [2, 3, 9, 5, 14];
Arr.sort(function (a, b) {
    if (a > b) {
        return 1;
    }
    if (a < b) {
        return -1;
    }
    return 0;
});
console.log(Arr);
// 2,3 => 2 - 3 => -ve => -1 => 2,3
//compare function

// a,b 
// a > b => a - b => +ve => 1 or 10
// a < b => a - b => -ve => -1
// a == b => a - b => 0

var str = ['ab', 'aa', 'ac', 'a']
str.sort(function (a, b) {
    if (a > b) {
        return -1;
    }
    if (a < b) {
        return 1;
    }
    return 0;
});
console.log(str);

// for numbers we can use shortcut
var arr = [2, 3, 9, 5, 14]
arr.sort(function (a, b) {
    return a - b;
});
console.log(arr);
