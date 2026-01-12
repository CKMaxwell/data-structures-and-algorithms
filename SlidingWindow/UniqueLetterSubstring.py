def Unique_Letter_Substring(input_str):
    left = 0
    right = 0
    counter = {}
    max_len = 0
    while right < len(input_str):
        print(counter)
        current_str = input_str[right]
        if current_str not in counter.keys():
            counter[current_str] = 1
            right += 1
        elif current_str in counter.keys():
            left += 1
            counter.pop(input_str[left])

        current_len = len(counter)
        if current_len > max_len:
            max_len = current_len
    return max_len
        

new_str = "thisishowwedoit"
a = Unique_Letter_Substring(new_str)
print(a)