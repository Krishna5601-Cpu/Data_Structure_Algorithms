// Base Square Pattern

for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= n; j++) {
    process.stdout.write("*");
  }
  console.log();
}

// 2. Right-Angled Triangle

for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= i; j++) {
    process.stdout.write("*");
  }
  console.log();
}

// 3. Numeric Right-Angled Triangle

for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= i; j++) {
    process.stdout.write(j + " ");
  }
  console.log();
}

// 4. Inverted Right-Angled Triangle

for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= n - i + 1; j++) {
    process.stdout.write("*");
  }
  console.log();
}

// 5. X Pattern

for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= n; j++) {
    if (i === j || i + j === n + 1) {
      process.stdout.write("*");
    } else {
      process.stdout.write(" ");
    }
  }
  console.log();
}

// 6. V Pattern

for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= 2 * n - 1; j++) {
    if (i === j || i + j === 2 * n) {
      process.stdout.write("*");
    } else {
      process.stdout.write(" ");
    }
  }
  console.log();
}

// 7.  Alphabet Right-Angled Triangle
for (let i = 1; i <= n; i++) {
  for (let j = 0; j < i; j++) {
    // String.fromCharCode converts ASCII values to characters
    process.stdout.write(String.fromCharCode(65 + j) + " ");
  }
  console.log();
}
