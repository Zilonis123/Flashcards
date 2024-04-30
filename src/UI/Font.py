import pygame, textwrap
    
"""
    The code defines a font class and functions to render and wrap text within a given rectangle on a
    Pygame surface.
    
    :param surface: The `surface` parameter in the functions `wrap_text` and `draw_text` represents the
    surface where the text will be rendered. In Pygame, a surface is a rectangular area where you can
    draw images, shapes, and text. It serves as the canvas on which you can display graphics
    :param text: The `text` parameter in the functions `wrap_text` and `draw_text` represents the text
    that you want to display on the screen. It is a string that contains the actual text content that
    you want to render within the specified rectangle on the pygame surface
    :type text: str
    :param color: The `color` parameter in the functions `wrap_text` and `draw_text` represents the
    color of the text that will be rendered on the surface. It is a string parameter that specifies the
    color of the text using color names or RGB values. For example, you can pass "white", "
    :type color: str
    :param rect: The `rect` parameter in the functions `wrap_text` and `draw_text` represents a
    rectangle where the text will be contained or drawn. It is of type `pygame.Rect`, which is a
    rectangle that can be used to define areas in a surface. The rectangle is defined by its top-left
    :type rect: pygame.Rect
    :param font: The `font` class is used to create a font object with a specified font name and size.
    The `render_text` method within the `font` class is used to render text using the specified font and
    color, returning a tuple containing the rendered text surface and its corresponding rectangle
    :type font: font
    :param pos: The `pos` parameter in both `wrap_text` and `draw_text` functions represents the
    position where the text will be rendered on the surface. It is a tuple containing the x and y
    coordinates of the top-left corner of the text bounding box
    :type pos: tuple[int, int]
"""

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
    


