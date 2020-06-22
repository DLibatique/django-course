// var carInfo = {
//   make: "Toyota",
//   year: 1990,
//   model: "Camry"
// }
// //
// // // console.log(carInfo["make"]); // need to pass in string, not var, to access key
// // //
// // // var myNewO = {
// // //   a: "hello",
// // //   b: [1, 2, 3],
// // //   c: {inside: ['a', 'b']}
// // // }
// // //
// // // console.log(myNewO["a"]);
// // // console.log(myNewO["b"][1]);
// // // console.log(myNewO["c"]["inside"][1]);
// //
// carInfo["year"] = 2006
// console.log(carInfo);
//
// carInfo["year"] += 1;
// console.log(carInfo);
//
// console.dir(carInfo); // display whole object
//
// // iterate through an object: use for in
//
// for (key in carInfo) { // but objects are not ordered
//   console.log(key);
//   console.log(carInfo[key]);
// }
//
// // object = {key: value}

// object methods

// var carInfo = {
//   make: "Toyota",
//   year: 1990,
//   model: "Camry",
//   carAlert: function(){ // call method directly on object
//     alert("We've got a car here!")
//   }
// }
//
// // this keyword (similar to self in python classes)
//
// var myObj = {
//   prop: 37,
//   reportProp: function(){
//     return this.prop
//   }
// }
//
// console.log(myObj.reportProp());
//
// //
//
// var simple = {
//   prop: "Hello",
//   myMethod: function(){
//     console.log("The myMethod was called");
//   }
// }
//
// simple.myMethod()

var myObj = {
  name: "Daniel",
  greet: function(){
    console.log("Hello " + this.name);
  }
}

myObj.greet()
