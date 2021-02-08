def double_string(data: list) -> int:
    counter = 0
    for i in data:
        center = int(len(i)/2)
        connected_left = i[:center]
        connected_right = i[center:]
        
        if connected_left in data and connected_right in data:
            counter += 1

    return counter

def ds(data: list) -> int:
    return len([x for x in data if x[:int(len(x)/2)] in data and x[int(len(x)/2):] in data])


print(ds(['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']))