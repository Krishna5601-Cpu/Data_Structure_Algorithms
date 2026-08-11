const prompt = require("prompt-sync")();

let num = Number(prompt("Enter num: "));

let ans = 0;
let i = 0;

while (num > 0) {
  let bit = num & 1;
  ans = bit * Math.pow(10, i) + ans;
  num = num >> 1;
  i++;
}

console.log(`Answer is: ${ans}`);
