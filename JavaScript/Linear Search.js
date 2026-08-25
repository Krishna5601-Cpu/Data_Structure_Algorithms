const prompt = require("prompt-sync")();
function search(arr, target) {
  // Linear search to find target in array
  for (let element of arr) {
    if (element === target) {
      return true;
    }
  }
  return false;
}

function getValidNumber(promptMessage, isPositive = false) {
  while (true) {
    const input = prompt(promptMessage);
    const num = Number(input);

    if (isNaN(num)) {
      alert("Please enter a valid number");
      continue;
    }

    if (isPositive && num <= 0) {
      alert("Please enter a positive number");
      continue;
    }

    return num;
  }
}

function main() {
  // Get array size with validation
  const arrSize = getValidNumber("Enter array size:", true);

  // Get array elements
  const numsArr = [];
  console.log("Enter array elements:");
  for (let i = 0; i < arrSize; i++) {
    const element = getValidNumber(`Element ${i + 1}:`);
    numsArr.push(element);
  }

  // Get target
  const target = getValidNumber("Enter target:");

  // Search and display result
  const found = search(numsArr, target);

  if (found) {
    console.log("Target is present in array");
  } else {
    console.log("Target was not found in array");
  }
}

// Run the program
main();
