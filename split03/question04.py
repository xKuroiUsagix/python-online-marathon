def divisor(num: int):
    for i in range(1, num + 1):
        if not num % i:
            yield i
    yield None


for i in divisor(25):
    print(i)