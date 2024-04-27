from src.UI.Flashcard import Flashcard
import pygame
from colors import ColorWheel


class render():

    def __init__(self) -> None:
        self.SIZE = (1280, 720)
        self.CENTER = (self.SIZE[0]//2, self.SIZE[1]//2)
        self.screen = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()
        self.running = True



        self.tick = 0

        self.wheel = ColorWheel()



        self.flashcard_Qs = [{"question":"5+5=?", "answer": "10"},
                           {"question":"5*5=?", "answer": "25"},
                           {"question":"10/5=?", "answer": "2"},
                           {"question":"5-5=?", "answer": "0"}]

        self.flashcards = self.generate_flashcards(self.flashcard_Qs)

    def generate_flashcards(self, QnA: list[dict]) -> list[Flashcard]:
        flashcards = []

        for i in range(len(QnA)):
            qna = QnA[i]
            q = qna["question"]
            a = qna["answer"]

            flashcards.append(Flashcard(self, q, a, active=True if i == 0 else False))

        return flashcards

    def get_next_color(self):
        wheel_next = tuple(self.wheel.next().rgb)
        color = pygame.Color(wheel_next)
        return color
    

    def next_flashcard(self) -> None:
        flashcard = self.flashcards.pop(0)
        flashcard.active = False
        self.flashcards.append(flashcard)

        self.flashcards[0].active = True


    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_NUMLOCK:
                    self.next_flashcard()

            for flashcard in self.flashcards:
                flashcard.tick_event(event)

    def draw(self) -> None:
        # RENDER
        # temporary surface that supports alpha 🐺
        surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)

        for flashcard in self.flashcards:
            flashcard.draw(self, surface)
        
        self.screen.blit(surface, (0,0))

    def run(self) -> None:
        while self.running:
            self.events()

            self.draw()

            # tick
            for flashcard in self.flashcards:
                flashcard.tick(self)

            pygame.display.flip()
            self.clock.tick(60)
            self.tick += 1

        pygame.quit()


if __name__ == "__main__":
    pygame.init()

    render().run()