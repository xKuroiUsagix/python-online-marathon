def kthTerm(n: int, k: int) -> int:
    pows = [n**0]
    i = 1
    while True:
        temp = pows[:]
        pows.append(n**i)
        for j in temp:
            pows.append(n**i + j)

        print(pows)
        i += 1
        if len(pows) >= k:
            return pows[k - 1]


print(kthTerm(3, 7))