import pygame, textwrap

class font:
    def __init__(self, font_name="freesansbold.ttf", font_size=32) -> None:
        self.font = pygame.font.Font(font_name, font_size)
        self.font_name = font_name

    def render_text(self, font_text: str, color="white") -> tuple[pygame.Surface, pygame.Rect]:
        text = self.font.render(font_text, True, color)
        text_rect = text.get_rect()

        return (text, text_rect)



def wrap_text(surface, text: str, color: str, rect: pygame.Rect, font: font, pos: tuple[int, int]):
    """
    Wraps text so it fits inside a rect
    """
    rect = pygame.Rect(rect)
    
    size: tuple[int, int] = font.font.size(text)
    text_height: int = size[1]
    full_text_width: int = size[0]
    l_width: int = full_text_width//len(text)+1
    
    wrapper = textwrap.TextWrapper(width=rect.w//l_width-3)

    text_list: list[str] = wrapper.wrap(text)
    
    for i in range(len(text_list)):
        element = text_list[i]
     
        t, t_rect = font.render_text(element, color)
        t_rect.center = pos
        t_rect.bottom += i*text_height

        surface.blit(t, t_rect)
    
    




def draw_text(surface, text: str, color: str, rect: pygame.Rect, font: font, pos: tuple[int, int]) -> pygame.Rect:
    """
    Draws text inside a rect
    """
    rect = pygame.Rect(rect)
    
    size: tuple[int, int] = font.font.size(text)
    full_text_width: int = size[0]
    l_width: int = full_text_width//len(text)
    
    if full_text_width > rect.w:
        c: int = 1*(len(text)-rect.w//l_width)
        text: str = text[c:len(text)]
    
     
    t, t_rect = font.render_text(text, color)
    t_rect.topleft = pos

    surface.blit(t, t_rect)
    
    return t_rect
    


