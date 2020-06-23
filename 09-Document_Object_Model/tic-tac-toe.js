// restart game button

var restart = document.querySelector("#b");

// grab all the squares

var squares = document.querySelectorAll("td");

// clear all the squares

function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = '';
  }
}

restart.addEventListener("click", clearBoard)

// check the square marker (blank, X, or O)

function changeMarker() {
  if (this.textContent === '') {
    this.textContent = 'X';
  } else if (this.textContent === "X") {
    this.textContent = "O";
  } else {
    this.textContent = '';
  }
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener("click", changeMarker);
}


// FOLLOWING WORKS IF COPIED 8 TIMES BUT VIOLATES DRY:
//
// var cellOne = document.querySelector("#one")
//
// cellOne.addEventListener("click", function(){
//   if (cellOne.textContent === '') {
//     cellOne.textContent = 'X';
//   } else if (cellOne.textContent === "X") {
//     cellOne.textContent = "O";
//   } else {
//     cellOne.textContent = '';
//   }
// })

// for loop to add event listeners to all the squares















// var boxes = document.querySelectorAll(".board-box");
// console.log(boxes)
//
// var selection = document.querySelector(".board-box");
// console.log(selection);
//
// var boxesOther = document.getElementsByTagName('td');
// console.log(boxesOther);
// console.log(boxesOther["3"]);
//
// for (var i = 0; i < 9; i++) {
//   var selection = boxes[i.toString()]
//   selection.addEventListener("click", function(){
//     if (selection.textContent === "") {
//       selection.textContent = "X";
//     } else if (selection.textContent === "X") {
//       selection.textContent = "O";
//     } else {
//       selection.textContent = "";
//     }
//   })
// }


// for (selection in boxes) {
//   selection.addEventListener("click", function(){
//   if (selection.textContent === "") {
//     selection.textContent = "X";
//   } else if (selection.textContent === "X") {
//     selection.textContent = "O";
//   } else {
//     selection.textContent = "";
//   }
//   })
// }
