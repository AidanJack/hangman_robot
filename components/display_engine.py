import pygame
import math

class DisplayEngine():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.center = (self.width // 2, self.height // 2)
        self.screen, self.clock = self.init_window()
        self.font = pygame.font.SysFont(None, 30)
    
    def init_window(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        #screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        clock = pygame.time.Clock()
        pygame.display.set_caption("Smiley Face")
        return screen, clock
    
    def test_touch(self, pos):
        my_rect = pygame.Rect(self.center[0]-50, self.center[1]-50, 100, 100)
        touched = my_rect.collidepoint(pos)
        color = (255,0,0) if touched == True else (100,0,0)
        pygame.draw.rect(self.screen, color, my_rect)
        
    def draw_face(self):
        face_radius = 100
        eye_radius = 10
        eye_offset_x = 30
        eye_offset_y = 40
        mouth_rect = pygame.Rect(self.center[0] - 50, self.center[1] + 20, 100, 50)
        
        # Eyes
        pygame.draw.circle(self.screen, (255,255,255), (self.center[0] - eye_offset_x, self.center[1] - eye_offset_y), eye_radius)
        pygame.draw.circle(self.screen, (255,255,255), (self.center[0] + eye_offset_x, self.center[1] - eye_offset_y), eye_radius)
        
        # Smile
        pygame.draw.arc(self.screen, (255,255,255), mouth_rect, math.radians(200), math.radians(340), 3)
        
    def draw_gameboard(self, hidden_word, available_letters, num_lives):
        lives_pos = (40,40)
        lives = "X " * (num_lives - 1) + "X" if num_lives > 0 else "GAME OVER"
        self.blit_text(lives, lives_pos, (255,255,255))
        
        #hidden_word = "_ _ _ _ _ _"
        self.blit_text(hidden_word, (self.center[0] - 30, self.center[1]), (255,255,255))
        
        #available_letters = "a b c d e f g h i j k l m n o p q r s t u v w x t u v x y z"
        self.blit_text(available_letters, (self.center[0] - 300, self.center[1] + 100), (255,255,255))
        
    def blit_text(self, text, pos, text_color):
        img = self.font.render(text, True, text_color)
        self.screen.blit(img, pos)
if __name__ == "__main__":
    running = True
    disp_eng = DisplayEngine(800, 480)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False
        
        disp_eng.screen.fill('black')
        #disp_eng.draw_face()
        pos = pygame.mouse.get_pos()
        disp_eng.test_touch(pos)
        #disp_eng.draw_gameboard("_ _ _ _ _ _", "a b c d e f g h i j k l m n o p q r s t u v w x t u v x y z", 5)
        pygame.display.flip()
        disp_eng.clock.tick(60)
    pygame.quit()
