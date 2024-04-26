import pygame
from .Font import font, draw_text

class Input:
    def __init__(self, pos: tuple[int, int], size: tuple[int, int]) -> None:
        
        self.rect = pygame.Rect(pos, size)
        self.font = font()
        self.text = ""
        self.active = False


    def tick(self, event: pygame.event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN: 

            if event.key == pygame.K_BACKSPACE: 
                self.text = self.text[:-1] 
            else: 
                self.text += event.unicode

    def draw(self, screen) -> None:
        color_active = pygame.Color('lightskyblue3')
        color_passive = pygame.Color('chartreuse4')

        color = color_active if self.active else color_passive

        # draw box
        pygame.draw.rect(screen, color, self.rect)

        # draw text
        text, _ = self.font.render_text(self.text)
        draw_text(screen, text, (self.rect.x+5, self.rect.y+5))
        