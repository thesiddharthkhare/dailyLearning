// Arrow Functions
// const fun = () => {}

// Regular function 
function greet(greeting, name) {
    return `${greeting} from ${name}`;
};

var newGreet = (greeting, name) => {
    return `${greeting} from ${name}`;
};

var shortGreet = (greeting, name) =>  `${greeting} from ${name}`;
// for single statement

var square = x => x * x;
// for only one parameter 
console.log(square(5));

let greeting = () => `Hello`

// Object shorthand
var age = 23
var city = 'Bangalore'

var obj = {
    age,
    city,
}; // keys same as the name of the variable
console.log(obj);

// Default parameters
function Profile(name, age, salary = 10000) {
    let profObj = {
        name,
        age,
        salary,
    };
    console.log(profObj);
}
Profile("Pooja", 23)
Profile("Sharwan", 24, 50000)

//Discount 
function totalCost(itemsCost, discount = 0) {
    var totalCost = itemsCost - (discount * itemsCost) / 100;
    // if (itemsCost > 2999) {
    //     totalCost = itemsCost - (discount * itemsCost) / 100;
    // } else {
    //     totalCost = itemsCost;
    // }
}
totalCost(3000, 10);