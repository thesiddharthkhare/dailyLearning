// Higher Order Functions
// map, filter, forEach, reduce => arrays => input will be array

// map
var arr = [1,2,3,4,5, 6];
arr.map(function (num) {
    console.log(num);
});

var arr1 = [
    {name: "Post no 1", likes: 100},
    {name: "Post no 2", likes: 200},
    {name: "Post no 3", likes: 2000, comments: 100},
    {name: "Post no 4", likes: 300},
    {name: "Post no 5", likes: 200},
    {name: "Post no 6", likes: 400},
    {name: "Post no 7", likes: 400},
    {name: "Post no 8", likes: 100},
    {name: "Post no 9", likes: 700},
    {name: "Post no 10", likes: 2500, comments: 500},
    {name: "Post no 11", likes: 1200},
    {name: "Post no 12", likes: 3200},
]
arr1.map(function (post) {
    console.log(post);
})

arr1.map(function (post) {
    console.log(post.likes);
})

// 3 parameters => arr[i], i, arr
arr1.map(function (post, index) {
    console.log(post.likes, index);
});

var filteredList = arr1.filter(function (post, index) {
    return index > 3;
})
console.log(filteredList)

arr1.map(function (post, index) {
    console.log(post.comments, index);
});

// Optional Chaining
arr1.map(function (post, index) {
    console.log(post?.comments, index);
});

var person = {
    address: {
        street: "Gandhi Street",
        city: "Bangalore"
    },
};

console.log(person.address?.city); // if not present will not give error

var arr2 = [1, 2];
console.log(arr2[10])

// true ? 'boolean truthy' : 'falsy'
// Ternary Operator => if else 