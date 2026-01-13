def  bubble_sort(new_array):
    for i in range(0, len(new_array)-1):
        for j in range(len(new_array)-1, i, -1):
            right = new_array[j]
            left = new_array[j-1]
            if right < left:
                val_temp = new_array[j]
                new_array[j] = left
                new_array[j-1] = val_temp
    return new_array

input_array = [1,3,4,0,1,-1,30,5]
a = bubble_sort(input_array)
print(a)