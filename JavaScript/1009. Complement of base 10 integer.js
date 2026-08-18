/**
 * @param {number} n
 * @return {number}
 */
var bitwiseComplement = function (n) {
  if (n === 0) {
    return 1;
  }
  let m = n;
  let mask = 0;

  while (m != 0) {
    mask = (mask << 1) | 1;
    m = m >> 1;
  }

  let answer = ~n & mask;
  return answer;
};
