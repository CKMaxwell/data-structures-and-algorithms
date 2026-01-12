def array_of_arrays(in_array):
    result = []

    def helper(in_array):
        for val_array in in_array:
            if isinstance(val_array, list):
                helper(val_array)
            else:
                result.append(val_array)
    
    helper(in_array)
    return result


arrs = [[[["a", [["b", ["c"]], ["d"]]], [["e"]], [[["f", "g", "h"]]]]]]
a = array_of_arrays(arrs)
print(a)