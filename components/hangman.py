import string
import random
from english_words import get_english_words_set

class LetterNotAvailableException(Exception):
    def __init__(self, message='Letter not available.'):
        super().__init__(message)
        
class GameOverException(Exception):
    def __init__(self, message='Game Over: No more guesses.'):
        super().__init__(message)
        
class HangmanBoard():
    def __init__(self, vp, printToTerminal=False):
        # Define Constants
        self.LETTERS = list(string.ascii_lowercase)
        self.WORDS = list(get_english_words_set(['web2'], lower=True))
        self.vp = vp # Used to trigger voice lines
        self.MAX_GUESSES = 5

        # Debug Output
        self.printToTerminal = printToTerminal
        
        # Set Game Variables to Start of Game Value. Used for Restaring 
        self.setup()
            
    def setup(self):
        self.availableLetters = self.LETTERS
        self.remainingNumGuesses = self.MAX_GUESSES
        self.curWord = self.generateWord()
        self.curWordState = ['_' for l in self.curWord] # Used as a List Repressentation of the State of the Word with its Guesses for easy output
        if self.printToTerminal == True: self.printState()

    def makeGuess(self, letter: str) -> (str, int, int, list[str]): # Returns the letter guessed, the remaining guesses, and the index of the letter if correct. Index is None if guess is wrong
        # Check for invalid guess
        if self.remainingNumGuesses <= 0:
            raise GameOverException # Probably want a custom exception
        elif len(letter) != 1:
            raise ValueError('Can only guess 1 letter!')
        elif letter not in self.availableLetters:
            raise LetterNotAvailableException('That letter was already guessed!') # Probably want to make custom error for easy error handling.
        
        # Check if Guess was Correct
        idx = None
        if letter in self.curWord:
            idxs = [index for index, value in enumerate(self.curWord) if value == letter]
            for idx in idxs:
                self.curWordState[idx] = letter
            
            if self.remainingNumGuesses == self.MAX_GUESSES: self.vp.load_never_wrong() # Play audio for never having been wrong
            else: self.vp.load_right_after_wrong() # Play audio for correct guess after previously guessed wrong
        else: # Guess is incorrect
            self.remainingNumGuesses -= 1
            if self.remainingNumGuesses <= 0:
                # Displays End Game Screen and Audio
                self.triggerGameOver()
                self.vp.load_game_over()
            else:
                self.vp.load_wrong()
                
        # Allows for Printing Minimal Game Information to Terminal for Debugging
        if self.printToTerminal:
            self.printState()
        
        self.vp.play()
            
        self.availableLetters.remove(letter)
        return (letter, self.remainingNumGuesses, idx, self.curWordState)
        
    def triggerGameOver(self):
        if self.printToTerminal:
            print(f' \n GAME OVER \n The word was {self.curWord}')
    
    def printState(self):
        print(f'\n')
        print(f'{self.curWordState}  : Guesses Remaining {self.remainingNumGuesses}')

    def generateWord(self):
        idx = random.randint(0, len(self.WORDS))
        return self.WORDS.pop(idx)

if __name__ == "__main__":
    hangman = HangmanBoard()
    hangman.printToTerminal = True
    while True:
        letter = input(f'\n Guess a letter from the following \n {hangman.availableLetters} \n')
        hangman.makeGuess(letter)
