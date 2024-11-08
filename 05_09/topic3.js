// Documentation => refer MDN

var str = "Masai"
console.log(str.toUpperCase());
console.log(str.toLowerCase());

var str2 = "School"
console.log(str.concat(str2)); // +

var batch = "       Full Time       "
console.log(batch.trim())
// will remove the spaces before naf after not between

console.log(str.split());
console.log(str.split(""));

const str3 = "The quick brown fox jumps over the lazy dog.";
console.log(str3.split(" "));

var searchTerm = "dog"
console.log(str3.indexOf(searchTerm)); // Gives the first occurence

//Slice
console.log(str.slice(1, 3));
//will not include the ending index

var arr = [1, 2, 3];
arr[1] = 10;
console.log(arr[1]);
// mutable

var obj = {name : "Masai School"}
obj.name = "Masai"
console.log(obj.name)


str[1] = 'i';
console.log(str[1]);
// immutable
// will not update 