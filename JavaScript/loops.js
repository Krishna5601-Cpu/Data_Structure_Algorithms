const readLineSync = require("readline-sync");
// for loop for known iterations
// for (initialization; condition; updation) {
//   code;
// }

// for (start; end; change) {
//   code;
// }

// for (let i = 1; i <= 22; i++) {
//   console.log(i);
// }

// for (let i = 22; i >= 0; i--) {
//   console.log(i);
// }

// let i;
// for (i = 1; i <= 10; i++) {
//   console.log(i);
// }
// console.log("Fails at: ", i);

// const n = readLineSync.question("Enter n: \n");
// for (let i = 1; i <= n; i++) {
//   console.log("Hehe");
//   console.log("Himmi");
// }

// Sum of n natural numbers:
// const n = readLineSync.question("Enter n: \n");
// let sum = 0;
// for (let i = 1; i <= n; i++) {
//   sum = sum + i;
//   // sum += i
// }
// console.log("The sum is:", sum);

// Factorial n

// fact = 1;
// const n = readLineSync.question("Enter n: ");
// if (n === 0) {
//   console.log("0! = 1");
// } else {
//   for (let i = 1; i <= n; i++) {
//     fact *= i;
//   }
// }
// console.log("Factorial is: ", fact);

// Factors of a number
// let n = readLineSync.question("Enter n: ");
// if (n === 0) console.log("Zero have no factors");
// let factors = [];
// for (let i = 1; i <= Math.floor(n / 2); i++) {
//   if (n % i === 0) {
//     factors.push(i);
//   }
// }
// console.log(factors);
// factors.forEach((element) => {
//   console.log(element);
// });
// console.log(n);

// Prime Number
// let n = readLineSync.question("Enter n: ");
// if (n === 0) console.log("Zero");
// let flag = true;
// for (let i = 2; i <= Math.floor(n / 2); i++) {
//   if (n % i === 0) {
//     flag = false;
//     break;
//   }
// }
// if (flag === true) console.log("Prime");
// else {
//   console.log("Not Prime");
// }

// let isPrime = (n) => {
//   if (n <= 1) return false;
//   if (n === 2) return true;
//   if (n % 2 === 0) return false;
//   for (let i = 3; i <= Math.floor(Math.sqrt(n)); i += 2) {
//     if (n % i === 0) return false;
//   }
//   return true;
// };
// let n = readLineSync.question("Enter n: ");
// console.log(isPrime(n));

// while when number of iterations are unknown

// let input = readLineSync.question("I will not stop until exit \n ");
// input.toLocaleLowerCase();
// while (input !== "exit") {
//   input = readLineSync.question("I will not stop until exit  \n ");
//   console.log("hahahahahahahahahahaha");
// }

// Reverse of Digits
// num = readLineSync.question("Enter the number: ");
// let sum = 0;
// let rem = 0;
// while (num !== 0) {
//   rem = num % 10;
//   sum = sum * 10 + rem;
//   num = Math.floor(num / 10);
// }
// console.log(sum);

// Sum of Digits
// num = readLineSync.question("Enter the number: ");
// let sum = 0;
// let rem = 0;
// while (num !== 0) {
//   rem = num % 10;
//   sum = sum + rem;
//   num = Math.floor(num / 10);
// }
// console.log(sum);

// Strong Number
// let num = Number(readLineSync.question("Enter the number: "));
// let original = num;
// let sum = 0;
// let rem = 0;

// while (num > 0) {
//   rem = num % 10;

//   let fact = 1;
//   for (let i = 1; i <= rem; i++) {
//     fact = fact * i;
//   }

//   sum = sum + fact;
//   num = Math.floor(num / 10);
// }

// if (sum === original) {
//   console.log(`${original} is a Strong Number.`);
// } else {
//   console.log(`${original} is not a Strong Number.`);
// }

// Guess the number

// let random = Math.floor(Math.random() * 100 + 1);

// let guess;
// let attempt = 0;

// while (guess !== random) {
//   guess = Number(readLineSync.question("Enter your guess: "));
//   if (isNaN(guess) || guess === "") {
//     console.log("Invaild Input");
//     continue;
//   }
//   if (random === guess) {
//     console.log("Right Guess Wuhuuuuu :) ", random);
//     attempt++;
//     console.log("Attempt: ", attempt);
//     break;
//   } else if (random > guess) {
//     console.log("Guess Higher ");
//     attempt++;
//     console.log("Attempt: ", attempt);
//   } else if (random < guess) {
//     console.log("Guess Lower ");
//     attempt++;
//     console.log("Attempt: ", attempt);
//   }
// }


