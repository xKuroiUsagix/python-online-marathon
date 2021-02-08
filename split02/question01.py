def ds(data: list) -> int:
    return len([x for x in data if x[:int(len(x)/2)] in data and\
                                   x[int(len(x)/2):] in data])