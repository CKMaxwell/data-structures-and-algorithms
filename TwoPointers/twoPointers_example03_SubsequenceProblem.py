def isSubsequence(str1, str2):
    str1_pointer = 0
    str2_pointer = 0
    
    while (str1_pointer <  len(str1)) and (str2_pointer < len(str2)):
        if str1[str1_pointer] != str2[str2_pointer]:
            str2_pointer += 1
        elif str1[str1_pointer] == str2[str2_pointer]:
            str1_pointer += 1
            str2_pointer += 1
    if  str1_pointer == len(str1):
        return True
    elif str1_pointer != len(str1):
        return False

a = isSubsequence('hello', 'helloDear')
b = isSubsequence('book', 'brooklyn')
c = isSubsequence('abc', 'cab')
print(a, b, c)