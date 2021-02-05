def isPalindromeNew(word: str) -> bool:
    letters = set(word)
    is_only_one = False

    if len(word) % 2 == 0:
        for i in letters:
            if word.count(i) % 2 != 0:
                return False
    else:
        for i in letters:
            if word.count(i) % 2 != 0 and not is_only_one:
                is_only_one = True
            elif word.count(i) % 2 != 0 and is_only_one:
                return False

    return True
