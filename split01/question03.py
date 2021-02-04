from math import ceil


def isPalindrome(word: str):
    if word.startswith(word[::-1]):
        return True

    middle = ceil(len(word) / 2)
    if word[:middle].endswith(word[middle:]):
        return True

    if len(word) % 2:
        return word[middle:] == word[:middle-1]
    else:
        return word[middle:] == word[:middle]

    


print(isPalindrome('qqqrrrwww'))