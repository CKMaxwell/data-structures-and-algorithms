def same_frequency(str1, str2):
    """
    輸入兩個字串，確認其字母出現的頻率是否相同
    """
    counter1 = {}
    counter2 = {}
    for i in range(len(str1)):
        if str1[i] not in counter1.keys():
            counter1[str1[i]] = 1
        elif str1[i] in counter1.keys():
            counter1[str1[i]] += 1
    for i in range(len(str2)):
        if str2[i] not in counter2.keys():
            counter2[str2[i]] = 1
        elif str2[i] in counter2.keys():
            counter2[str2[i]] += 1
    if counter1 == counter2:
        return True
    elif counter1 != counter2:
        return False

a = same_frequency("abab", "aabb")
b = same_frequency("aaab", "abab")
c = same_frequency("abbb", "bbba")
d = same_frequency("abcd", "abcdefg")
print(a, b, c, d)