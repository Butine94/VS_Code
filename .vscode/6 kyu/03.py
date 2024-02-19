class Robot:
    def __init__(self, word):
        self.word = word
    
    def learnWord(self, seen):
        seen = ()
        if not all(letter.isalpha() for letter in self.word):
            return 'I do not understand the input'
        elif self.word not in seen:
            return f'Thank you for teaching me {self.word}'
            seen.add(self.word)
        else:
            return f'I already know the word {self.word}'