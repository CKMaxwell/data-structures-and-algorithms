import copy
def insertion_sort(input_arr):
    for i in range(1, len(input_arr)):
        key = copy.deepcopy(input_arr[i])
        j = i-1
        while (j >= 0) and (input_arr[j] > key):
            input_arr[j+1] = input_arr[j]
            j -= 1
        input_arr[j+1] = key
    return input_arr

new_array = [14, -4, 17, 6, 22, 1, -5]
a = insertion_sort(new_array)
print(a)