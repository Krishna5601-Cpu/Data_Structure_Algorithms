const prompt = require("prompt-sync")();

let binary = parseInt(prompt("Enter the binary number: "), 10);

let decimal = 0;
let base = 1;

while (binary > 0) {
  let digit = binary % 10;

  if (digit !== 0 && digit !== 1) {
    console.log("Invalid binary input!");
    process.exit(1);
  }

  if (digit === 1) {
    decimal += base;
  }

  base *= 2;
  binary = Math.floor(binary / 10);
}

console.log(`Decimal: ${decimal}`);
