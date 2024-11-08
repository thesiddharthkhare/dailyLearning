// Desturcturing
//In arrays
var numsArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
var [first, second] = numsArr;
console.log(first)

// Objects
var profile = {
    firstName: "Hani",
    lastName: "Thakkar",
    age: 22,
    posts: [{title: "Post no 1", likes: 100}],
    account: "Facebook",
};
// console.log(profile.firstName)
const {firstName, lastName, age, ...remaining} = profile;
console.log(lastName);
console.log(remaining);
