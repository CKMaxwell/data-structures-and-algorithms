def average_pair(list_input, goal):
    count = 0
    for i in range(len(list_input)):
        for j in range(i+1, len(list_input)):
            # print(list_input[i], list_input[j])
            average = (list_input[i] + list_input[j]) / 2
            if average == goal:
                count += 1
    return count

def average_pair_pointer(list_input, goal):
    count = 0
    pointer_left = 0
    pointer_right = len(list_input) - 1
    
    while (pointer_left < pointer_right):
        average = (list_input[pointer_left] + list_input[pointer_right]) / 2
        
        if average > goal:
            pointer_right -= 1
        elif average < goal:
            pointer_left += 1
        elif average == goal:
            count += 1
            pointer_right -= 1
            pointer_left += 1
    return count

test_input = [-11, 0, 1, 2, 3, 9, 14, 17, 21]
goal = 1.5
ans = average_pair(test_input, goal)
ans2 = average_pair_pointer(test_input, goal)
print(ans, ans2)