from src.UI.Font import font, draw_text
from src.UI.Input import Input

import pygame
from colors import ColorWheel

def get_next_color(wheel: ColorWheel):
    wheel_next = tuple(wheel.next().rgb)
    prim = pygame.Color(wheel_next)
    return prim

def run() -> None:
    pygame.init()
    SIZE = (1280, 720)
    CENTER = (SIZE[0]//2, SIZE[1]//2)
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    running = True

    sansbold = font("./lib/fonts/coolvetica.otf")

    text_input = Input(
        (CENTER[0]-150, CENTER[1]+100), 
        (300, sansbold.font.get_height()+10),
        sansbold)

    tick = 0

    wheel = ColorWheel()
    primary_color = get_next_color(wheel)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not text_input.active: 
                if event.key == pygame.K_r:
                    primary_color = get_next_color(wheel)

            text_input.tick_event(event)

        screen.fill(primary_color)

        # RENDER
        # temporary surface that supports alpha 🐺
        surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

        text, text_rect = sansbold.render_text("TEXT", CENTER)
        draw_text(surface, text, text_rect)

        text_input.draw(surface, tick)

        # tick
        text_input.tick(tick)

        screen.blit(surface, (0,0))

        pygame.display.flip()
        clock.tick(60)
        tick += 1

    pygame.quit()


if __name__ == "__main__":
    run()