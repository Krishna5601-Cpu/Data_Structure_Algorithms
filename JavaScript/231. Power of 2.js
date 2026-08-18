var isPowerOfTwo = function (n) {
  // Method 1: While loop
  if (n <= 0) return false;
  while (n % 2 === 0) {
    n /= 2;
  }
  return n === 1;

  // Method 2: Bit manipulation (most efficient)
  // return n > 0 && (n & (n - 1)) === 0;
};
