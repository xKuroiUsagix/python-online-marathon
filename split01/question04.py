# not solved yet
def findPermutation(n: int, p: list, q: list) -> list:
    return [p.index(q[x]) + 1 for x in range(n)]


print(findPermutation(5, [3, 4, 1, 2, 5], [4, 5, 2, 3, 1]))
