from math import floor
def merge(a1, a2):
    result  = []
    i = 0
    j = 0
    while (i < len(a1)) and (j < len(a2)):
        if a1[i] >= a2[j]:
            result.append(a2[j])
            j += 1
        elif a1[i] < a2[j]:
            result.append(a1[i])
            i += 1
    # 處理剩餘數據
    while (i < len(a1)):
        result.append(a1[i])
        i += 1
    while (j < len(a2)):
        result.append(a2[j])
        j += 1
    return result

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        middle = floor(len(arr)/2)
        left = arr[0: middle]
        right = arr[middle:]
        return merge(merge_sort(left), merge_sort(right))
a = merge([1, 15, 17], [-3, 9, 16])
print(a)

input_arr = [15, 3, 17, 18, 0, 36, -336, 1054, 35]
b = merge_sort(input_arr)
print(b)