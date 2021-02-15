class Gallows:
    def __init__(self, words=[], game_over=False) -> None:
        self.words = words
        self.game_over = game_over

    
    def play(self, word: str):
        try:
            if word in self.words or not word.startswith(self.words[-1][-1]):
                self.game_over = True
                return 'game over'
            else:
                self.words.append(word)
                return self.words
        except IndexError:
            self.words.append(word)
            return self.words


    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'