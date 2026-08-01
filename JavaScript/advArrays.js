const readLineSync = require("readline-sync");
// Advance Array Questions -

/**
 * 1. Left rotation by 1 element
 */

// let arr = [1, 2, 3, 4, 5];
// for (let i = 0; i < arr.length; i++) {
//   if (i == 0) {
//     arr[i] = arr[arr.length - 1];
//   }
//   if (i == arr.length) {
//     arr[arr.length] = arr[0];
//   }

//   arr[i] = arr[i + 1];

// }

// [2,3,4,5,undefined]

// console.log(arr);

// let arr = [1, 2, 3, 4, 5];
// let copy = arr[0];
// for (let i = 0; i < arr.length; i++) {
//   if (i === arr.length - 1) {
//     arr[arr.length - 1] = copy;
//   } else {
//     arr[i] = arr[i + 1];
//   }
// }
// // [2,3,4,5,1]
// console.log(arr);

// let arr = [1, 2, 3, 4, 5];
// let copy = arr[0];
// for (let i = 0; i < arr.length - 1; i++) {

//   arr[i] = arr[i + 1];

// }
// arr[arr.length - 1] = copy;

// // [2,3,4,5,1]
// console.log(arr);

/**
 * 2. Right rotation by 1 element
 */

// let arr1 = [1, 2, 3, 4, 5];
// let copy1 = arr1[arr1.length - 1];
// for (let i = arr1.length - 1; i > 0; i--) {
//   arr1[i] = arr1[i - 1];
// }

// arr1[0] = copy1;

// // [ 5, 1, 2, 3, 4 ]
// console.log(arr1);

// Nested Logic -

// for (let i = 1; i <= 10; i++) {
//   console.log(`i: ${i}`);
//   for (let j = 1; j <= 10; j++) {
//     console.log(`j: ${j}`);
//   }
// }

/**
 * Left rotation by k element -
 */

// let arr = [1, 2, 3, 4, 5];
// let num = readLineSync.question("Enter num: ");
// num = num % arr.length;

// for (let i = 1; i <= num; i++) {

//   let temp = arr[0];
//   for (let i = 0; i <= arr.length - 1; i++) {
//     if (i === arr.length - 1) {
//       arr[arr.length - 1] = temp;
//     } else {
//       arr[i] = arr[i + 1];
//     }

//   }

// }

// console.log(arr);

/**
 * Right rotation by k elements -
 */

// let arr = [1, 2, 3, 4, 5];
// let num = Number(readLineSync.question("Enter num: "));
// num = num % arr.length;

// for (let i = 1; i <= num; i++) {
//   let temp = arr[arr.length - 1];

//   for (let j = arr.length - 1; j > 0; j--) {
//     arr[j] = arr[j - 1];
//   }

//   arr[0] = temp;
// }

// console.log(arr);

