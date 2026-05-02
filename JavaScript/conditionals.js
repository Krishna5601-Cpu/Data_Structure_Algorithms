// let age = Number(prompt("Enter your age: "));

// if (isNaN(age)) {
//   console.log("Invalid Input: ");
// }

// if (age >= 18) {
//   console.log("You can vote");
// } else {
//   console.log("You cannot vote");
// }

// let amount = prompt("Enter amount: ");

// if (amount < 0) {
//   console.log("Mat kr lala mt kr");
// }

// if (amount > 0 && amount <= 5000) {
//   console.log(amount);
// } else if (amount > 5000 && amount <= 7000) {
//   console.log(amount - (5 / 100) * amount);
// } else if (amount > 7000 && amount <= 9000) {
//   console.log(amount - (10 / 100) * amount);
// } else if (amount < 9000) {
//   console.log(amount - (20 / 100) * amount);
// }

// let unit = Number(prompt("Enter units "));
// let amount;
// if (unit >= 400) {
//   amount = (unit - 400) * 13;
//   amount = 400;
// }

// if (unit >= 200 && unit < +400) {
//   amount = amount + (unit - 200) * 8;
//   unit = 200;
// }

// if (unit >= 100 && unit < +200) {
//   amount = amount + (unit - 100) * 6;
//   unit = 100;
// }

// amount = amount + unit * 4;

// console.log(amount);

// let amount = parseInt(prompt("Enter the amount: "));
// let originalAmount = amount; // Keep a copy for the final display

// let fiveHun = 0;
// let twoHun = 0;
// let hun = 0;
// let fifty = 0;
// let ten = 0;
// let one = 0;

// // Check for 500s
// if (amount >= 500) {
//   fiveHun = Math.floor(amount / 500);
//   amount = amount % 500;
// }

// // Check for 200s
// if (amount >= 200) {
//   twoHun = Math.floor(amount / 200);
//   amount = amount % 200;
// }

// // Check for 100s
// if (amount >= 100) {
//   hun = Math.floor(amount / 100);
//   amount = amount % 100;
// }

// // Check for 50s
// if (amount >= 50) {
//   fifty = Math.floor(amount / 50);
//   amount = amount % 50;
// }

// // Check for 10s
// if (amount >= 10) {
//   ten = Math.floor(amount / 10);
//   amount = amount % 10;
// }

// // Check for 1s
// if (amount >= 1) {
//   one = Math.floor(amount / 1);
//   amount = amount % 1;
// }

// console.log(`Total Amount: ₹${originalAmount}`);
// console.log(
//   `500: ${fiveHun}, 200: ${twoHun}, 100: ${hun}, 50: ${fifty}, 10: ${ten}, 1: ${one}`,
// );

console.log(12 > 13 ? "true" : "false");
console.log(122 > 13 ? "true" : "false");


