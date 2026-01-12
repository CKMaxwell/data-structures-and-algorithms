test_arr = [15, 3, 17, -17, 18, 20, 2, 1, 666]
def partition(p, r):
    x = test_arr[r]  # pivot
    i = p - 1
    for j in range(p, r):
        if (test_arr[j] <= x):
            i += 1
            # 交換arr[i], arr[j]
            temp = test_arr[i]
            test_arr[i] = test_arr[j]
            test_arr[j] = temp
    # 交換arr[i+1] arr[r]
    temp = test_arr[i+1]
    test_arr[i+1] = test_arr[r]
    test_arr[r] = temp

    return i + 1

def quick_sort(p, r):
    if (p < r):
        q = partition(p, r)
        quick_sort(p, q-1)
        quick_sort(q+1, r)

quick_sort(0, len(test_arr)-1)
print(test_arr)