/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

//Elmo :: Ryan Lee, Emily Ortiz
//SoftDev pd8
//K29 -- Getting more comfortable with the dev console and the DOM
//2023-04-19w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j + x;
};

//console.log(f(5));


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };
//console.log(o['age']);


var addItem = function(text) {//changes the html and adds the text variable as another list element
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

//addItem("this is text");


var removeItem = function(n) {//removes element at index n
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};

//removeItem(0);


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

//red();


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};


//insert your implementations here for...
// FIB
function fib(n){
  if (n == 0){
      return 0;
  } else if (n == 1) {
      return 1;
  } else{
      return fib(n - 2) + fib(n - 1);
  }
}

// FAC
function fact(n){
  if (n < 2){
      return 1;
  } 
  return n * fact(n - 1); 
}

// GCD
function gcd(a, b){
  if (a % b === 0){
    return b;
  }
  return gcd(b, a%b);
}

// console.log(gcd(2,2));//2
// console.log(gcd(4,2));//2
// console.log(gcd(2,4));//2
// console.log(gcd(1,1));//1
// console.log(gcd(7,5));//1
// console.log(gcd(64,40));//8

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};
addItem(fib(5));
addItem(fact(5));
addItem(gcd(5,10));
var dasbut = document.getElementById("b");
dasbut.addEventListener('click', ()=>{addItem("fib of 5 is: " + fib(5))});
dasbut.addEventListener('click', ()=>{addItem("factorial of 5 is: " + fact(5))});
dasbut.addEventListener('click', ()=>{addItem("gcd of 5 and 10 is: " + gcd(5,10))});
var st = document.getElementById("s");
s.addEventListener('click', ()=>{stripe()});
//()=>{console.log()}
