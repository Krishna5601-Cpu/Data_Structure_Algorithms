const arr1 = [1, 2, 3, 4, 5];

const arr2 = new Array(1, 2, 3);

const arr3 = Array.of(1, 2, 3);

const arr4 = Array.from("hello");

console.log(arr1);
console.log(arr2);
console.log(arr3);
console.log(arr4);

// ACCESSING ELEMENTS

const nums = [10, 20, 30, 40];

console.log(nums[0]);
console.log(nums[nums.length - 1]);

// ADDING ELEMENTS

let fruits = ["Apple", "Banana"];

fruits.push("Mango");
fruits.unshift("Orange");

console.log(fruits);

// REMOVING ELEMENTS

fruits.pop();

fruits.shift();

console.log(fruits);

// INSERT / DELETE USING SPLICE

let colors = ["Red", "Blue", "Green"];

colors.splice(1, 0, "Yellow");

colors.splice(2, 1);

console.log(colors);

// SLICE

const numbers = [1, 2, 3, 4, 5];

const part = numbers.slice(1, 4);

console.log(part);

// CONCAT

const a = [1, 2];
const b = [3, 4];

const merged = a.concat(b);

console.log(merged);

// SPREAD OPERATOR

const spreadMerged = [...a, ...b];

console.log(spreadMerged);

// FIND LENGTH

console.log(numbers.length);

// LOOPING METHODS

const values = [10, 20, 30];

// for
for (let i = 0; i < values.length; i++) {
  console.log(values[i]);
}

// for...of
for (const value of values) {
  console.log(value);
}

// forEach
values.forEach((value, index) => {
  console.log(index, value);
});

// MAP

const doubled = values.map((value) => value * 2);

console.log(doubled);

// FILTER

const even = [1, 2, 3, 4, 5, 6].filter((num) => num % 2 === 0);

console.log(even);

// REDUCE

const sum = [1, 2, 3, 4, 5].reduce((acc, curr) => acc + curr, 0);

console.log(sum);

// FIND

const firstEven = [1, 3, 5, 6, 7].find((num) => num % 2 === 0);

console.log(firstEven);

// FIND INDEX

const index = [1, 3, 5, 6, 7].findIndex((num) => num === 6);

console.log(index);

// SOME

const hasEven = [1, 3, 5, 6].some((num) => num % 2 === 0);

console.log(hasEven);

// EVERY

const allPositive = [1, 2, 3, 4].every((num) => num > 0);

console.log(allPositive);

// INCLUDES

console.log([1, 2, 3].includes(2));

// INDEXOF

console.log([10, 20, 30].indexOf(20));

// LASTINDEXOF

console.log([1, 2, 1, 3].lastIndexOf(1));

// REVERSE

const rev = [1, 2, 3];

rev.reverse();

console.log(rev);

// SORT

const unsorted = [5, 2, 8, 1];

unsorted.sort((a, b) => a - b);

console.log(unsorted);

// TO SORT DESCENDING

unsorted.sort((a, b) => b - a);

console.log(unsorted);

// JOIN

console.log(["a", "b", "c"].join("-"));

// SPLIT TO ARRAY

const str = "apple,banana,mango";

const fruitsArray = str.split(",");

console.log(fruitsArray);

// FLAT

const nested = [1, [2, [3, [4]]]];

console.log(nested.flat(3));

// FLATMAP

const flatMapped = [1, 2, 3].flatMap((num) => [num, num * 2]);

console.log(flatMapped);

// FILL

const filled = new Array(5).fill(0);

console.log(filled);

// COPYWITHIN

const cp = [1, 2, 3, 4, 5];

cp.copyWithin(0, 3);

console.log(cp);

// ARRAY DESTRUCTURING

const data = [10, 20, 30];

const [first, second, third] = data;

console.log(first, second, third);

// REST OPERATOR

const [head, ...tail] = [1, 2, 3, 4, 5];

console.log(head);
console.log(tail);

// REMOVE DUPLICATES

const duplicates = [1, 2, 2, 3, 4, 4];

const unique = [...new Set(duplicates)];

console.log(unique);

// MAX VALUE

const max = Math.max(...[5, 8, 3, 9, 1]);

console.log(max);

// MIN VALUE

const min = Math.min(...[5, 8, 3, 9, 1]);

console.log(min);

// ARRAY TO OBJECT

const users = [
  { id: 1, name: "Krishna" },
  { id: 2, name: "John" },
];

const userMap = Object.fromEntries(users.map((user) => [user.id, user]));

console.log(userMap);

// GROUP BY

const people = [
  { name: "A", age: 20 },
  { name: "B", age: 20 },
  { name: "C", age: 21 },
];

const grouped = Object.groupBy(people, (person) => person.age);

console.log(grouped);

// FREQUENCY COUNTER

const freq = {};

for (const item of [1, 1, 2, 2, 2, 3]) {
  freq[item] = (freq[item] || 0) + 1;
}

console.log(freq);

// CHUNK ARRAY

function chunk(array, size) {
  const result = [];

  for (let i = 0; i < array.length; i += size) {
    result.push(array.slice(i, i + size));
  }

  return result;
}

console.log(chunk([1, 2, 3, 4, 5, 6], 2));

//
// SHUFFLE ARRAY

function shuffle(array) {
  const copy = [...array];

  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));

    [copy[i], copy[j]] = [copy[j], copy[i]];
  }

  return copy;
}

console.log(shuffle([1, 2, 3, 4, 5]));

// INTERSECTION

function intersection(arr1, arr2) {
  return arr1.filter((item) => arr2.includes(item));
}

console.log(intersection([1, 2, 3], [2, 3, 4]));

//
// DIFFERENCE

function difference(arr1, arr2) {
  return arr1.filter((item) => !arr2.includes(item));
}

console.log(difference([1, 2, 3], [2, 3, 4]));

// UNION

function union(arr1, arr2) {
  return [...new Set([...arr1, ...arr2])];
}

console.log(union([1, 2], [2, 3]));

// ROTATE ARRAY

function rotate(arr, k) {
  k %= arr.length;

  return [...arr.slice(-k), ...arr.slice(0, -k)];
}

console.log(rotate([1, 2, 3, 4, 5], 2));

// IS ARRAY

console.log(Array.isArray([]));
console.log(Array.isArray({}));

// ARRAY AT METHOD

const letters = ["a", "b", "c", "d"];

console.log(letters.at(-1));

// TO SORTED (IMMUTABLE)

const sortedCopy = [4, 2, 1, 3].toSorted((a, b) => a - b);

console.log(sortedCopy);

// TO REVERSED (IMMUTABLE)

const reversedCopy = [1, 2, 3].toReversed();

console.log(reversedCopy);

// TO SPLICED (IMMUTABLE)

const splicedCopy = [1, 2, 3, 4].toSpliced(1, 2);

console.log(splicedCopy);

// WITH (IMMUTABLE REPLACE)

const updated = [1, 2, 3].with(1, 100);

console.log(updated);
