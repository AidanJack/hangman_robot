from components.hangman import HangmanBoard
from components.audio_player import VoicePlayer
from components.display_engine import DisplayEngine
import pygame
import time

vp = VoicePlayer("/home/aidan/projects/hangman_robot/audio/")
game = HangmanBoard(vp)
display = DisplayEngine(800, 480)

pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not pygame.mixer.get_busy():
            guess = display.check_collisions(pygame.mouse.get_pos())
            print(f'guessed: {guess}')
            if guess is not None:
                game.makeGuess(guess)
                print(f'game_state: {game.getGameState()}')
    
    display.screen.fill('black')
    display.update_display(*game.getGameState())
    pygame.display.flip()
    time.sleep(1/60)
