// For Loop
//    1          2     3
for(var i = 0; i < 5; i++) {
    // 4
    console.log(i);
}

// 1. initialisation => i=0
// 2. condition => i<5
// 3. increment/decrement => iteration
// 4. code block

// 1. => var i = 0, i = 1, i = 2......

// 1 2 4 3 2 4 3 2 4 3 .....

var movies = ['Avengers', 'Dr Strange', 'Thor', 'Loki', 'Deadpool', 'Iron Man', 'Hulk', 'Superman', 'Spiderman']

for (var i = 0; i < movies.length; i++) {
    // console.log(movies[i]);
}

for (var i = 0; i < movies.length; i++) {
    if (i == 3) {
        continue;
    }
    console.log(movies[i]);
}

// continue => will skip only that condition
// break => breaks out of the loop on meeting the condition

for (var i =0; i < movies.length; i++) {
    if (i > 2) {
        continue;
    }
    console.log(movies[i]);
} // will give the same output as break