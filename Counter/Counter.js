function intersection(arr1, arr2) {
  let result = [];
  let arr3 = arr1.concat(arr2);
  let counter = {};
  for (let i = 0; i < arr3.length; i += 1) {
    if (!counter[arr3[i]]) {
      counter[arr3[i]] = 1;
    } else {
      counter[arr3[i]] += 1;
    }
  }
  // loop over counter
  for (let property in counter) {
    if (counter[property] >= 2) {
      result.push(property);
    }
  }
  return result;
}

let arr1 = [1, 2, 3, 7, 9, 19, 25];
let arr2 = [5, 16, 10, 3, 1, 19];
let test1 = intersection(arr1, arr2);
console.log(test1);
