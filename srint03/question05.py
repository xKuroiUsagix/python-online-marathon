def logger(func):
    def wrapper(*args, **kwargs):
        info = ''
        to_return = func(*args, **kwargs)
        for i in args:
            info += str(i) + ', '

        for key in kwargs:
            info += str(kwargs[key]) + ', '
    
        print(f'Executing of function {func.__name__} with arguments {info[:-2]}...')
        return to_return

    return wrapper


@logger
def concat(*args, **kwargs):
    connected = ''
    for i in args:
        connected += str(i)
    for key in kwargs:
        connected += str(kwargs[key])
    return connected