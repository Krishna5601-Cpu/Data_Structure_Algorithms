const reverseArr = (arr) => {
  let i = 0;
  let j = arr.length - 1;

  while (i < j) {
    let temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    i++;
    j--;
  }
};

let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

console.log("Array before reversing: ");
for (let i = 0; i < 10; i++) {
  console.log(nums[i]);
}

reverseArr(nums);

console.log("Array after reversing: ");
for (let i = 0; i < 10; i++) {
  console.log(nums[i]);
}
