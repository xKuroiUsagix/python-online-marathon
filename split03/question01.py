def outer(name: str):
    def inner():
        print(f'Hello, {name}')

    return inner


outer('Tom')()