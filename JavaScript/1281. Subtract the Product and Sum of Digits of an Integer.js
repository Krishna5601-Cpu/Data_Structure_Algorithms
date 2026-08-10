/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function (n) {
  let sum = 0;
  let product = 1;

  while (n > 0) {
    let rem = n % 10;
    sum += rem;
    product *= rem;
    n = Math.floor(n / 10);
  }

  return product - sum;
};
