from src.UI.Font import font, draw_text
from src.UI.Input import Input

import pygame
from colors import ColorWheel


class render():

    def __init__(self) -> None:
        self.SIZE = (1280, 720)
        self.CENTER = (self.SIZE[0]//2, self.SIZE[1]//2)
        self.screen = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.coolvetica = font("./lib/fonts/coolvetica.otf")

        self.text_input = Input(
            (self.CENTER[0]-150, self.CENTER[1]+100), 
            (300, self.coolvetica.font.get_height()+10),
            self.coolvetica)

        self.tick = 0

        self.wheel = ColorWheel()
        self.primary_color = ""
        self.get_next_color()

    def get_next_color(self):
        wheel_next = tuple(self.wheel.next().rgb)
        self.primary_color = pygame.Color(wheel_next)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and not self.text_input.active: 
                if event.key == pygame.K_r:
                    self.get_next_color()

            self.text_input.tick_event(event)

    def draw(self):
        self.screen.fill(self.primary_color)

        # RENDER
        # temporary surface that supports alpha 🐺
        surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)

        text, text_rect = self.coolvetica.render_text("TEXT", self.CENTER)
        surface.blit(text, text_rect)

        self.text_input.draw(surface, self.tick)

        self.screen.blit(surface, (0,0))

    def run(self) -> None:
        while self.running:
            self.events()

            self.draw()
            
            # tick
            self.text_input.tick(self.tick)


            pygame.display.flip()
            self.clock.tick(60)
            self.tick += 1

        pygame.quit()


if __name__ == "__main__":
    pygame.init()

    render().run()