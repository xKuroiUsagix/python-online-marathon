def filterBible(scripture: list, book: str, chapter: str) -> list:
    filtered = []
    for scr in scripture:
        if scr.startswith(book + chapter):
            filtered.append(scr)

    return filtered