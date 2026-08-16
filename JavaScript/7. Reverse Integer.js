/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  const INT_MAX = 2147483647;
  const INT_MIN = -2147483648;

  let answer = 0;

  while (x !== 0) {
    let digit = x % 10;
    x = Math.trunc(x / 10);

    if (
      answer > Math.trunc(INT_MAX / 10) ||
      answer < Math.trunc(INT_MIN / 10)
    ) {
      return 0;
    }

    answer = answer * 10 + digit;
  }

  return answer;
};
