function swapAlternate(arr, size) {
  for (let i = 0; i < size; i += 2) {
    if (i + 1 < size) {
      // Swap using destructuring assignment
      [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
    }
  }
}

// Using readline for user input
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log("Enter array elements (10 numbers): ");

let numsArr = [];
let count = 0;

rl.on("line", (input) => {
  numsArr.push(parseInt(input));
  count++;

  if (count === 10) {
    console.log("\nBefore swap:");
    console.log(numsArr.join("\n"));

    swapAlternate(numsArr, 10);

    console.log("\nAfter swap:");
    console.log(numsArr.join("\n"));

    rl.close();
  }
});
