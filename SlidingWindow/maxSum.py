def max_min_Sum(input_list, number):
    max_val = None
    min_val = None

    for i in range(0, len(input_list)-(number-1)):
        new_list = input_list[i: i+number]
        print(new_list)
        if max_val is None:
           max_val = sum(new_list)
        elif max_val is not None:
           if sum(new_list) > max_val:
               max_val = sum(new_list)
        if min_val is None:
            min_val = sum(new_list)
        elif min_val is not None:
            if sum(new_list) < min_val:
                min_val = sum(new_list)
    return (max_val, min_val)

a = max_min_Sum([2, 7, 3, 0, 6, 1, -5, -12, -11], 3)
print(a)