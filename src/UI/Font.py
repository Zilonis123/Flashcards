import pygame

class font:
    def __init__(self, font_name="freesansbold.ttf", font_size=32) -> None:
        self.font = pygame.font.Font(font_name, font_size)

    def render_text(self, font_text: str, pos: tuple[int, int]= (0,0), color="white") -> tuple[pygame.Surface, pygame.Rect]:
        text = self.font.render(font_text, True, color)
        text_rect = text.get_rect()
        text_rect.center = pos

        return (text, text_rect)

def draw_text(screen, text: pygame.Surface, text_rect: pygame.Rect) -> None:
    screen.blit(text, text_rect)