// While Loop

// iT STARTS WITH A ACONDITION

var movies = ['Avengers', 'Dr Strange', 'Thor', 'Loki', 'Deadpool', 'Iron Man', 'Hulk', 'Superman', 'Spiderman']

var j = 0;
while (j < movies.length) {
    // console.log(movies[j]);
    j++;
}

var j = 0;
while (j  < movies.length) {
    if (j == 3) {
        break;
    }
    // console.log(movies[j]);
    j++;
}

var j = 0;
while (j < movies.length) {
    console.log(movies[j]);
    j++;
    if (j == 3) {
        j++;
        continue;
    }
}

