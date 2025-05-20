def print_fibonacci(length=10):
    if length == 0:
        print([])
        return

    a, b = 0, 1
    result = []
    for _ in range(length):
        result.append(a)
        a, b = b, a + b
    print(result)
