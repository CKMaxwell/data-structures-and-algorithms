function sameFrequency(str1, str2) {
  // 輸入兩個字串，確認其字母出現的頻率是否相同
  let arr1 = str1.split("");
  let arr2 = str2.split("");
  if (arr1.length != arr2.length) {
    return false;
  }
  let counter1 = {};
  let counter2 = {};
  for (let i = 0; i < arr1.length; i += 1) {
    if (counter1[arr1[i]]) {
      counter1[arr1[i]] += 1;
    } else {
      counter1[arr1[i]] = 1;
    }
  }
  for (let i = 0; i < arr2.length; i += 1) {
    if (counter2[arr2[i]]) {
      counter2[arr2[i]] += 1;
    } else {
      counter2[arr2[i]] = 1;
    }
  }
  for (let property in counter1) {
    if (!counter2[property]) {
      return false;
    }
    if (counter2[property] !== counter1[property]) {
      return false;
    }
  }
  return true;
}

let a = sameFrequency("abab", "aabb");
let b = sameFrequency("aaab", "abab");
let c = sameFrequency("abbb", "bbba");
let d = sameFrequency("abcd", "abcdefg");
console.log(a, b, c, d);
