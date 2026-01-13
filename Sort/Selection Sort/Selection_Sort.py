def selection_sort(input_arr):
    for i in range(0, len(input_arr)-1):
        min_ind = i
        for j in range(i, len(input_arr)):
            if input_arr[j] < input_arr[i]:
                min_ind = j
        temp_val = input_arr[i]
        input_arr[i] = input_arr[min_ind]
        input_arr[min_ind] = temp_val
    return input_arr

new_array = [14, -4, 17, 6, 22, 1, -5]
a = selection_sort(new_array)
print(a)