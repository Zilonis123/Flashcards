from src.UI.UI import font, draw_text

import pygame


def run() -> None:
    pygame.init()
    SIZE = (1280, 720)
    CENTER = (SIZE[0]//2, SIZE[1]//2)
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    running = True

    sansbold = font()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")

        # RENDER
        text, text_rect = sansbold.render_text("TEXT", CENTER)
        draw_text(screen, text, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    run()