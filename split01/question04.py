def findPermutation(n: int, p: list, q: list) -> list:
    return [p.index(q[x]) + 1 for x in range(n)]