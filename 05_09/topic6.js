// prefix and postfix

// i++, j++ => postfix
// ++i, ++j, --k => prefix

var x = 5;
//x = 5
var y = x++;
//y = 5
//x = x++ = 6
// after this operation is document, x will be incremented
console.log(x);
console.log(y);

var p = 5;
//p=5
var q = ++p;
// p = p+1 = 6
// q = 6
console.log(p);
console.log(q);

var a = 2;
// a=2
var b = 3 + ++a;
// ++a => a = a+1 => 3
// 3+3=b=6
console.log(a);
console.log(b);
