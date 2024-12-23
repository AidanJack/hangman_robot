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
        # screen = pygame.display.set_mode((self.width, self.height))
        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.mouse.set_visible(False)
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
        
    def draw_gameboard(self, hidden_word, available_letters, num_lives, pos):
        lives_pos = (40,40)
        lives = "X " * (num_lives - 1) + "X" if num_lives > 0 else "GAME OVER"
        self.blit_text(lives, lives_pos, (255,255,255))
        
        #hidden_word = "_ _ _ _ _ _"
        self.blit_text(hidden_word, (self.center[0] - 30, self.center[1]), (255,255,255))
        
        fonts = self.letter_to_font(available_letters, (255,255,255))
        l_dim = (fonts[0].get_width(), fonts[0].get_height())

        letter_center = (self.center[0], self.center[1] + 80)
        num_letters = len(available_letters)
        letter_spacing = 15

        line_width = num_letters * l_dim[0] + letter_spacing * (num_letters - 1)
        starting_point = (letter_center[0] - line_width// 2, letter_center[1])

        self.apply_fonts(fonts, starting_point, letter_spacing)

        # text_rect = self.blit_text(available_letters, self.center, (255,255,255))
        # print(f'widht: {text_rect.get_width()}')
        # print(text_rect.get_height())
    
    def letter_to_font(self, letters, text_color):
        fonts = []
        for l in letters:
            f_surf = self.font.render(l, True, text_color)
            fonts.append(f_surf)
        return fonts


    def blit_text(self, text, pos, text_color):
        img = self.font.render(text, True, text_color)
        self.screen.blit(img, pos)
        return img
    
    def apply_fonts(self,fonts, start, spacing):
        cur_x = start[0]
        for f in fonts:
            cur_x += f.get_width() + spacing
            self.screen.blit(f, (cur_x, start[1]))

if __name__ == "__main__":
    running = True
    pos = (0,0)
    disp_eng = DisplayEngine(800, 480)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
        
        disp_eng.screen.fill('black')
        #disp_eng.draw_face()
        # disp_eng.test_touch(pygame.mouse.get_pos())
        disp_eng.draw_gameboard("_ _ _ _ _ _", "aaaaaaaaaaaaaaaaaaaaaaaa", 5, pos)
        # disp_eng.draw_gameboard("_ _ _ _ _ _", "a b c d e f g h i j k l m n o p q r s t u v w x t u v x y z", 5)
        pygame.display.flip()
        disp_eng.clock.tick(60)
    pygame.quit()
