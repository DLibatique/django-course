function hello(){
  console.log("hello world!");
}

hello()

function helloYou(name){
  console.log('hello '+name);
}

helloYou() // name undefined
helloYou("Daniel")

function addNum(num1, num2) {
  console.log(num1+num2);
}

addNum(3, 5)
addNum("hello","world") // data type too loose, so it will concatenate, see e.g.:
addNum("2", 2) // type coercion

function helloSomeone(name="Frankie") { // assign default parameters
  console.log("Hello " + name);
}

helloSomeone("Daniel")
helloSomeone()

function formal(name="Sam", title="Sir") {
  console.log(title + " " + name);
}

formal()
console.log("Welcome" + formal()) // formal() isn't returning something here

function formalActual(name="Sam", title="Sir") {
  return title + " " + name // gives an output
}

console.log(formalActual())
console.log("Welcome " + formalActual())

function timesFive(numInput) {
  var result = numInput * 5
  return result
}

console.log(timesFive(4));
var answer = timesFive(10);
console.log(answer);

SCOPE: if variable is defined w/i function, it exists only w/i that function (local scope)

GLOBAL SCOPE

var v = " GLOBAL V"
var stuff = "GLOBAL STUFF"

function fun(stuff) {
  console.log(v);
  stuff = "Reassign stuff inside func"
  console.log(stuff);
}

fun();
console.log(stuff) // global variable not affected by use in local function
