import pygame

class font:
    def __init__(self, font_name="freesansbold.ttf", font_size=32) -> None:
        self.font = pygame.font.Font(font_name, font_size)
        self.font_name = font_name

    def render_text(self, font_text: str, color="white") -> tuple[pygame.Surface, pygame.Rect]:
        text = self.font.render(font_text, True, color)
        text_rect = text.get_rect()

        return (text, text_rect)



def wrap_text(surface, text: str, color: str, rect: pygame.Rect, font: font, pos: tuple[int, int]) -> pygame.Rect:
    """
    Wraps text so it fits inside a rect
    """
    # NOTE To future self: "Please don't blame me if this doesn't work for you because it barely worked for me
    # also by saying this I hereby don't have any guilt if this breaks"
    rect = pygame.Rect(rect)
    
    size: tuple[int, int] = font.font.size(text)
    full_text_width: int = size[0]
    l_width: int = full_text_width//len(text)+1
    
    if full_text_width > rect.w:

        completed = False
        i=0
        while not completed:
            try:
                writable: str = text[i*rect.w//l_width:(i+1)*rect.w//l_width]
                text = text[i*rect.w//l_width:-1]
            except:
                writable: str = text[i*rect.w//l_width:-1]
                completed = True
            t, t_rect = font.render_text(writable, color)
            t_rect.center = (pos[0], pos[1]+(t_rect.h*i))

            surface.blit(t, t_rect)
            i+=1
            if i>100:
                break
    
     
    t, t_rect = font.render_text(text, color)
    t_rect.center = pos

    surface.blit(t, t_rect)
    
    return t_rect
    




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
    


