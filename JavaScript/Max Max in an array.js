function getMax(arr) {
  let max = -Infinity;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= max) {
      max = arr[i];
    }
  }
  return max;
}

function getMin(arr) {
  let min = Infinity;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] <= min) {
      min = arr[i];
    }
  }
  return min;
}

// Using readline for user input in Node.js
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Enter the array size: ", (size) => {
  size = parseInt(size);
  console.log("Enter array elements: ");

  let num = [];
  let count = 0;

  rl.on("line", (input) => {
    num.push(parseInt(input));
    count++;

    if (count === size) {
      let maximum = getMax(num);
      let minimum = getMin(num);
      console.log(`Max: ${maximum} Min: ${minimum}`);
      rl.close();
    }
  });
});
