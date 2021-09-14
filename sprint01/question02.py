def filterBible(scripture: list, book: str, chapter: str) -> list:
    return [scr for scr in scripture if scr.startswith(book + chapter)]
