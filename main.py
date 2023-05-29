def fibonacci(n):
    if n < 0:
        raise ValueError("n deve ser maior do que zero")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_2 = 0
        fib_1 = 1
        fib_n = 0

        for _ in range(2, n + 1):
            fib_n = fib_1 + fib_2
            fib_2 = fib_1
            fib_1 = fib_n

        return fib_n