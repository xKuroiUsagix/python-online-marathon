import random


def randomWord(words: list):
    while not len(words):
        yield None
    while True:
        temp = words[:]
        while True:
            choice = random.choice(temp)
            del temp[temp.index(choice)]
            yield choice