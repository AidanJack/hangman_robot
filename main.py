from components.hangman import HangmanBoard
from components.audio_player import VoicePlayer

vp = VoicePlayer("/home/aidan/projects/robot/audio/")
game = HangmanBoard(vp, printToTerminal=True)
vp.load_intro()
vp.play()
while True:
    letter = input(f'\n Guess a letter from the following \n {game.availableLetters} \n')
    game.makeGuess(letter)
