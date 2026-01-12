def fibonacci_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        val = fibonacci_sequence(n-1) + fibonacci_sequence(n-2)
        return val

for i in range(15):
    print(fibonacci_sequence(i))