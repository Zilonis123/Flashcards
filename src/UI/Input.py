import pygame
from .Font import font, draw_text

class Input:
    def __init__(self, pos: tuple[int, int], size: tuple[int, int], font: font) -> None:
        
        self.rect = pygame.Rect(pos, size)
        self.font = font
        self.text = ""
        self.active = False

        self._backspace_down = False


    def tick_event(self, event: pygame.event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if not self.active:
            return

        if event.type == pygame.KEYDOWN: 

            if event.key == pygame.K_BACKSPACE: 
                self._backspace_down = True
            else: 
                self.text += event.unicode

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                self._backspace_down = False
        
    def tick(self, tick: int) -> None:
        if self._backspace_down == True and tick%2==0:
            self.text = self.text[:-1] 


    def draw(self, screen, tick: int) -> None:
        color_active = pygame.Color('lightskyblue3')
        color_passive = pygame.Color('chartreuse4')

        color = color_passive

        # draw box
        pygame.draw.rect(screen, color, self.rect)

        # draw text
        text_w = 0
        if len(self.text) > 0:
            text_rect = draw_text(screen, self.text, "white", self.rect, self.font, (self.rect.x+5,self.rect.y+5))
            text_w = text_rect.w

        # draw cursor
        if self.active and tick%60>30:
            x_pos = self.rect.x+5+text_w
            y = self.rect.y
            pygame.draw.line(screen, "gray", (x_pos, y+5), (x_pos, y-5+self.rect.height))
        