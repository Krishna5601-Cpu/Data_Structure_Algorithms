function findUnique(arr) {
  let ans = 0;
  for (let i = 0; i < arr.length; i++) {
    ans ^= arr[i]; // XOR operator in JavaScript
  }
  return ans;
}
