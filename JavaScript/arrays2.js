const prompt = require("prompt-sync")();
// Sum of n element -
// let n = prompt("Enter n: ");
// let sum = 0;

// for (let i = 0; i <= n; i++) {
//   sum = sum + i;
// }

// console.log(`Sum is ${sum}`);

// Sum of n element of aaray -
// let sumArray = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1];
// let sum = 0;
// for (let i = 0; i < sumArray.length; i++) {
//   sum = sum + sumArray[i];
// }

// console.log(`Sum is ${sum}`);

// Max element of an array -
// let elements = [10, 20, 30, 40, 60, 50, 70, 80];
// let MAX = elements[0];
// for (let i = 1; i < elements.length; i++) {
//   if (elements[i] > MAX) {
//     MAX = elements[i];
//   }
// }
// console.log(`Max element is ${MAX}`);

// Min element of an array -
// let elements = [20, 10, 30, 7, 60, 50, 70, 80];
// let MIN = elements[0];
// for (let i = 1; i < elements.length; i++) {
//   if (elements[i] < MIN) {
//     MIN = elements[i];
//   }
// }
// console.log(`Min element is ${MIN}`);

// 1st and 2nd Max Elements an array -
// let elements = [10, 30, 40, 40, 40];
// let firstMax = elements[0];
// let secondMax = elements[1];

// for (let i = 0; i < elements.length; i++) {
//   if (elements[i] >= secondMax && elements[i] != firstMax) {
//     secondMax = elements[i];
//     if (elements[i] >= firstMax) {
//       secondMax = firstMax;
//       firstMax = elements[i];
//     }
//   }
// }

// console.log(firstMax);
// console.log(secondMax);

// 2nd Approach -
// let ele = [20, 10, 30, 7, 60, 50, 70, 80, 75];
// let max = Math.max(ele[0], ele[1]);
// let Smax = Math.min(ele[0], ele[1]);

// for (let i = 2; i < ele.length; i++) {
//   if (ele[i] > max) {
//     Smax = max;
//     max = ele[i];
//   } else if (ele[i] > Smax) {
//     Smax = ele[i];
//   }
// }

// console.log(`Max and Second Max are ${max}, ${Smax}`);

// Reverse Array -
// let ele = [20, 10, 30, 7, 60, 50, 70, 80, 75];
// let reversedArray = [];
// let index = 0;
// for (let i = ele.length - 1; i >= 0; i--) {
//   reversedArray.push(ele[i]);
// }

// console.log(reversedArray);

// let ele = [20, 10, 30, 7, 60, 50, 70, 80, 75];
// let reversedArray = [];
// let index = 0;
// for (let i = ele.length - 1; i >= 0; i--) {
//   reversedArray[index] = ele[i];
//   index++;
// }

// console.log(reversedArray);
// let ele = [20, 10, 30, 7, 60, 50, 70, 80, 75];
// let first = 0;
// let last = ele.length - 1;

// while (first < last) {
//   let temp = ele[first];
//   ele[first] = ele[last];
//   ele[last] = temp;

//   first++;
//   last--;
// }

// console.log(ele);

// All the zeros on the left and Ones on the right -
// let arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 0];
// let i = 0;
// let j = 0;
// for (let k = 0; k < arr.length; k++) {
//   if (arr[i] === 0) {
//     let temp = arr[i];
//     arr[i] = arr[j];
//     arr[j] = temp;
//     j++;
//   }
//   i++;
// }

// console.log(arr);
