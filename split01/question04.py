# not solved yet
def findPermutation(n: int, p: list, q: list) -> list:
    r = []
    for i in range(1, n+1):
        q[i] = p[r[i]]


findPermutation(3, [], [])
