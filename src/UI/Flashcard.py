import pygame
from .Font import font, wrap_text
from .Input import Input


class Flashcard():
    def __init__(self, render, question: str, answer: str, active=False, pos=(0,0)) -> None:
        self.question = question
        self.answer = answer
        self.active = active

        self.pos = pos
        self.CENTER = render.CENTER

        self.font = font("./lib/fonts/coolvetica.otf")
        self.text_input = Input(
            (render.CENTER[0]-150, render.CENTER[1]+100), 
            (300, self.font.font.get_height()+10),
            self.font)
        self.text_input.active = True
        
        # background
        background_color: pygame.Color = render.get_next_color()
        self.background = Background(background_color, render.SIZE)

    def change_pos(self, offset: tuple[int, int]) -> tuple[int, int]:
        self.pos = change_tuple(self.pos, offset)

        self.text_input.rect.topleft = change_tuple(self.text_input.rect.topleft, offset)
        self.background.rect.topleft = change_tuple(self.background.rect.topleft, offset)

        return self.pos
    
    def set_pos(self, pos: tuple[int, int]) -> tuple[int, int]:
        self.pos = pos

        self.text_input.rect.top = pos[1]+self.CENTER[1]+100
        self.background.rect.topleft = pos

        return self.pos

    def draw(self, render, screen: pygame.Surface) -> None:
        if not self.active: 
            return
        
        self.background.draw(screen)

        self.text_input.draw(screen, render.tick)

        # draw the question
        t, t_rect = self.font.render_text(self.question)
        t_rect.center = change_tuple(render.CENTER, self.pos)
        
        wrap_text(screen, self.question, "white", pygame.Rect((0,0), render.SIZE), self.font, change_tuple(render.CENTER, self.pos))

        # screen.blit(t, t_rect)

    def tick_event(self, event: pygame.event, render) -> bool:
        if not self.active: 
            return False
        
        if event.type == pygame.KEYDOWN:
            if event.key == 13:
                # ENTER
                render.next_flashcard()
                return True
        
        self.text_input.tick_event(event)
        return False


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

def change_tuple(tuple1: tuple[float, float], tuple2: tuple[float, float]) -> tuple[float, float]:
    return (tuple1[0]+tuple2[0], tuple1[1]+tuple2[1])