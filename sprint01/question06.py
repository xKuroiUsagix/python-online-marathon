def order(a: list) -> str:
    ascending = True
    descending = True
    for i in range(len(a) - 1):
        if not (a[i] >= a[i + 1] and descending):
            descending = False
        
        if not (a[i] <= a[i + 1] and ascending):
            ascending = False

    if ascending:
        return 'ascending'
    elif descending:
        return 'descending'
    else:
        return 'not sorted'
    
    
def order_other(a: list) -> str:
    sorted_a = sorted(a)

    if sorted_a == a:
        return "ascending"
    elif sorted_a[::-1] == a:
        return "descending"
    return "not sorted"
