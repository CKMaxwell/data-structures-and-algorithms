def isPalindrome(input_str):
    pointer_L = 0
    pointer_R = len(input_str) - 1
    while (pointer_L < pointer_R):
        if input_str[pointer_L] != input_str[pointer_R]:
            return False
        elif input_str[pointer_L] == input_str[pointer_R]:
            pointer_L += 1
            pointer_R -= 1
        return True

a = isPalindrome('abcdcba')
b = isPalindrome('aaaabbb')
c = isPalindrome('aaaabbbcdggdcbbbaaa')
print(a, b, c)