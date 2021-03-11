def filterBible(scripture: list, book: str, chapter: str) -> list:
    return [src for src in scripture if src.startswith(book + chapter)]