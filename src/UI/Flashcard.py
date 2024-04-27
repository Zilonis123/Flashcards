import pygame
from .Font import font
from .Input import Input


class Flashcard():
    def __init__(self, render, question: str, answer: str, active=False) -> None:
        self.question = question
        self.answer = answer
        self.active = active

        self.font = font("./lib/fonts/coolvetica.otf")
        self.text_input = Input(
            (render.CENTER[0]-150, render.CENTER[1]+100), 
            (300, self.font.font.get_height()+10),
            self.font)
        
        # background
        background_color: pygame.Color = render.get_next_color()
        self.background = Background(background_color, render.SIZE)

    def draw(self, render, screen: pygame.Surface) -> None:
        if not self.active: 
            return
        
        self.background.draw(screen)

        self.text_input.draw(screen, render.tick)

        # draw the question
        t, t_rect = self.font.render_text(self.question)
        t_rect.center = render.CENTER

        screen.blit(t, t_rect)

    def tick_event(self, event: pygame.event) -> None:
        if not self.active: 
            return
        
        self.text_input.tick_event(event)


    def tick(self, render) -> None:
        if not self.active: 
            return

        self.text_input.tick(render.tick)

class Background():
    def __init__(self, color: pygame.Color, size: tuple[int, int], pos=(0,0)) -> None:
        
        self.color = color
        self.rect = pygame.Rect(pos, size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)