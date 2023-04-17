//Elmo :: Ryan Lee, Emily Ortiz
//SoftDev pd8
//K27 -- Basic functions in JavaScript
//2023-04-03t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

function fact(n){
    if (n < 2){
        return 1;
    } 
    return n * fact(n - 1); 
}

// console.log(fact(1)); // 1
// console.log(fact(2)); // 2
// console.log(fact(3)); // 6
// console.log(fact(4)); // 24
// console.log(fact(5)); // 120

function fib(n){
    if (n == 0){
        return 0;
    } else if (n == 1) {
        return 1;
    } else{
        return fib(n - 2) + fib(n - 1);
    }
}

console.log(fib(0)); // 0
console.log(fib(1)); // 1
console.log(fib(2)); // 1
console.log(fib(3)); // 2
console.log(fib(4)); // 3