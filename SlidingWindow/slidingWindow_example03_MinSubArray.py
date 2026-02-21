def MinSubArray(inList, Lbound):
    index_L = 0
    index_R = 0
    min_len = len(inList) + 1
    current_sum = 0
    while index_R < len(inList):
        current_sum += inList[index_R]
        while (current_sum >= Lbound):
            if (index_R+1)-index_L < min_len:
                min_len = (index_R+1)-index_L
            # 找到長度，開始處理下一個sub list
            current_sum -= inList[index_L]
            index_L += 1
        index_R += 1
    if min_len == len(inList)+1:
        return 0
    else:
        return min_len

    # while index_L < len(inList):
    # while index_R < len(inList):
    #     sub_list = inList[index_L:index_R]
    #     print(sub_list)
    #     if (sum(sub_list) > Lbound):
    #         if (index_R+1)-index_L < min_sub:
    #             min_sub = (index_R+1)-index_L
    #             print(min_sub)
    #             break
    #     elif (sum(sub_list) < Lbound):
    #         index_R += 1
    # index_L += 1
    # return min_sub

input_list = [8, 1, 6, 15, 3, 16, 5, 7, 14, 30, 12]
min_sum = 60
a = MinSubArray(input_list, min_sum)           # 答案=4
b = MinSubArray([9, 8, 1, 4, 9, 5, 1, 2], 11)  # 答案=2
print(a, b)