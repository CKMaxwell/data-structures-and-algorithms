// 從輸入的array中，找到兩個數字，其平均剛好是第二個輸入的參數
// 需要找到所有可能的組合
averagePair([-11, 0, 1, 2, 3, 9, 14, 17, 21], 1.5);

function averagePair(arr, avg) {
  // 暴力解法
  // 複雜度:O(n^2)
  let result = [];
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if ((arr[i] + arr[j]) / 2 == avg) {
        result.push([arr[i], arr[j]]);
      }
    }
  }

  console.log(result);
  return result;
}

averagePairPointer([-11, 0, 1, 2, 3, 9, 14, 17, 21], 1.5);

function averagePairPointer(arr, avg) {
  // 使用two pointer
  // 複雜度:O(n)
  let left = 0;
  let right = arr.length - 1;
  let result = [];

  while (right > left) {
    let temp_avg = (arr[right] + arr[left]) / 2;
    if (temp_avg > avg) {
      right--;
    } else if (temp_avg < avg) {
      left++;
    } else if (temp_avg == avg) {
      result.push([arr[right], arr[left]]);
      right--;
      left++;
    }
  }

  console.log(result);
  return result;
}
