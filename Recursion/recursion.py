def recursion(n):
    if n == 1:
        return 10
    elif n > 1:
        val = recursion(n-1) + 15
        return val

a = recursion(3)
b = recursion(4)
c = recursion(5)
print(a, b, c)