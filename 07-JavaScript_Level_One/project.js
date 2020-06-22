var firstName = prompt("What is your first name?")
var lastName = prompt("What is your last name?")
var age = prompt("What is your age?")
var height = prompt("What is your height?")
var petName = prompt("What is your pet's name?")

if (firstName[0] === lastName[0] && age > 20 && age < 30 && height >= 170 && petName[petName.length-1] === "y") {
  console.log("You're a spy!")
} else {
  console.log("What are you checking here for?")
}

alert("Thanks!")
