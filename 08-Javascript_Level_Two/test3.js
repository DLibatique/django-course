var country1 = "USA"
var country2 = "Germany"
var country3 = "China"

var countries = ["USA", "Germany", "China"]
var countriesMulti = ["USA",
                    "Germany",
                    "China"]

console.log(countries[1])
console.log(countries[2]);

countries[2] = "France"

console.log(countries);

// immutable vs. mutable:
// an array is mutable but a string is immutable

console.log(country1[2]);
country1[2] = "B";
console.log(country1);

var mixed = [true, 20, "string"]

console.log(mixed);
console.log(mixed.length);

// array methods
var myArr = ['one', 'two', 'three']

// to remove:
var lastItem = myArr.pop()
console.log(lastItem);
console.log(myArr);

// to add:
myArr.push('new item')
console.log(myArr);
console.log(myArr[myArr.length-1]);

// nested arrays
var matrix = [[1,2,3], [4,5,6], [7,8,9]]
console.log(matrix[0][2]);

// array iteration
var arr = ["A", "B", "C"]

// regular for statement
for (var i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

// for of statement
for (i of arr) {
  console.log(i);
}

// pass items of array into a function: for each

for (letter of arr) {
  alert(letter);
}

// is equivalent to:

arr.forEach(alert); // no parentheses, just function name passed into .forEach

function addAwesome(name) {
  console.log(name+" is awesome!");
}

// another example

console.log(addAwesome("django"));

var topics = ['python', 'django', 'science']

console.log(topics.forEach(addAwesome));



// .forEach method, for of statement, pop and push methods to take off or add,
// nest arrays, take in mixed types, assignment for array elements
