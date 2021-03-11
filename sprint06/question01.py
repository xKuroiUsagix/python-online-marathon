import json


def add_uniq(dictionary, key, uniq):
    try:
        if isinstance(dictionary[key], list):
            for word in dictionary[key]:
                uniq.add(word)
        else:
            uniq.add(dictionary[key])
    except KeyError:
        uniq = []


def find(file, key):
    uniq = set()
    with open(file) as f:
        json_read = json.loads(f.read())
        
        if isinstance(json_read, list):
            for i in json_read:
                add_uniq(i, key, uniq)
        else:
            add_uniq(json_read, key, uniq)

    return list(uniq)