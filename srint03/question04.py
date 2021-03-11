def divisor(num: int):
    for i in range(1, num + 1):
        if not num % i:
            yield i

    while True:
        yield None