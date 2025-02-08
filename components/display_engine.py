import pygame
import math

class DisplayEngine():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.center = (self.width // 2, self.height // 2)
        self.screen, self.clock = self.init_window()
        self.font = pygame.font.SysFont(None, 30)
        self.letter_rects = []
    
    def init_window(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        # screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.mouse.set_visible(True)
        clock = pygame.time.Clock()
        pygame.display.set_caption("Smiley Face")
        return screen, clock
    
    def check_collisions(self, pos):
        for rect, letter in self.letter_rects:
            if rect.collidepoint(pos):
                return letter
        return None


    def update_display(self, hidden_word, available_letters, num_lives):
        lives_pos = (40,40)
        lives = "X " * (num_lives - 1) + "X" if num_lives > 0 else "GAME OVER"
        self.blit_text(lives, lives_pos, (255,255,255))
        
        #hidden_word = "_ _ _ _ _ _"
        hidden_word = ''.join(hidden_word)
        self.blit_text(hidden_word, (self.center[0] - 30, self.center[1]), (255,255,255))
        

        letter_spacing = 15

        letter_surfaces = [self.font.render(letter, True, (255, 255, 255)) for letter in available_letters]
        l_dim = (letter_surfaces[0].get_width(), letter_surfaces[0].get_height())
        line_width = len(letter_surfaces) * l_dim[0] + letter_spacing * (len(letter_surfaces) - 1)
        container_rect = pygame.Rect(0,0, line_width, l_dim[1])
        container_rect.center = (self.center[0], self.center[1] + 100)

        offset = container_rect.left
        self.letter_rects.clear()
        for i, l in enumerate(letter_surfaces):
            rect = l.get_rect(topleft=(offset, container_rect.top))
            self.letter_rects.append((rect, available_letters[i]))# Store rect for each letter
            offset += l.get_width() + letter_spacing
            self.screen.blit(l, rect)

        
    
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
    
    def apply_fonts(self, fonts, start, spacing):
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
