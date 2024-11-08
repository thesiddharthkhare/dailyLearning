var profile = {
    firstName: "Hani",
    lastName: "Thakkar",
    age: 22,
    posts: [{title: "Post no 1", likes: 100},
            {title: "Post no 2", likes: 200},

    ],
    account: "Facebook",
};
// console.log(profile.firstName)
const {firstName, 
    lastName,
    posts:[{likes}, {likes: likes2}],
} = profile;
console.log(likes)
console.log(likes2)