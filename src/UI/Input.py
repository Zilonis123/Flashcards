import pygame
from .Font import font, draw_text

# The `Input` class represents an input field with text entry functionality and the `Checkbox` class
# represents a checkbox with on/off state.

class Input:
    def __init__(self, pos: tuple[int, int], size: tuple[int, int], text_font: font) -> None:
        
        self.rect = pygame.Rect(pos, size)
        self.font = text_font
        self.font_small = font(self.font.font_name, 24)
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
        color_passive = pygame.Color((200,200,200))
        color_active = pygame.Color('#0492c2')

        color = color_passive if not self.active else color_active

        # draw box
        pygame.draw.rect(screen, color, self.rect, width=3, border_radius=7)

        # draw label
        t, t_rect = self.font_small.render_text("Answer", color)
        t_rect.bottomleft = self.rect.topleft
        # t_rect.bottom -= t_rect.height
        screen.blit(t, t_rect)

        # draw text
        text_w = 0
        if len(self.text) > 0:
            text_rect = draw_text(screen, self.text, "white", self.rect, self.font, (self.rect.x+5,self.rect.y+5))
            text_w = text_rect.w

        # draw cursor
        if self.active and tick%60>30:
            x_pos = self.rect.x+5+text_w
            y = self.rect.y
            pygame.draw.line(screen, color, (x_pos, y+5), (x_pos, y-5+self.rect.height))
        

class Checkbox():
    def __init__(self, pos: tuple[int, int], size: tuple[int, int]) -> None:
        self.rect = pygame.Rect(pos, size)
        self.text = ""
        self.active = False # on / off

    def tick_event(self, event):
        pass

    def draw(self, screen, tick):
        pass