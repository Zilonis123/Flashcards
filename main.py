from src.UI.Flashcard import Flashcard
import pygame, requests
from colors import ColorWheel

def get_questions() -> list:
    def replace_html_entities(text):
        replacements = {
            '&#039;': "'",
            '&quot;': '"'
        }
        for entity, replacement in replacements.items():
            text = text.replace(entity, replacement)
        return text

    url = "https://opentdb.com/api.php?amount=50&category=9&type=boolean"
    data = requests.get(url).json()
    

    QnA = []
    for item in data["results"]:
        question = {"question": replace_html_entities(item["question"]), "answer":item["correct_answer"]}
        QnA.append(question)

    return QnA
class render():

    def __init__(self, questions: list[dict]) -> None:
        self.SIZE = (980, 720)
        self.CENTER = (self.SIZE[0]//2, self.SIZE[1]//2)
        self.screen = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()
        self.running = True



        self.tick = 0

        self.wheel = ColorWheel()



        self.flashcard_Qs = questions

        self.flashcards = self.generate_flashcards(self.flashcard_Qs)

        self.chaningFlashcards = False

    
            

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
        self.flashcards.append(flashcard)

        self.flashcards[0].active = True
        self.flashcards[0].set_pos((0,self.SIZE[1]))

        self.chaningFlashcards = True
        self.tick = 0


    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_NUMLOCK and not self.chaningFlashcards:
                    self.next_flashcard()

            if not self.chaningFlashcards:
                for flashcard in self.flashcards:
                    dobreak = flashcard.tick_event(event, self)
                    if dobreak: break

    def draw(self) -> None:
        # RENDER
        # temporary surface that supports alpha 🐺
        surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        surface.fill("black")

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

            if self.chaningFlashcards:
                transition_frames = 30

                sped = self.SIZE[1]/transition_frames
                self.flashcards[0].change_pos((0, -sped))
                self.flashcards[-1].change_pos((0, -sped))

                if self.tick == transition_frames:
                    self.chaningFlashcards = False
                    self.flashcards[0].set_pos((0,0))
                    self.flashcards[-1].active = False

            pygame.display.flip()
            self.clock.tick(60)
            self.tick += 1

        pygame.quit()


if __name__ == "__main__":
    pygame.init()

    print("Getting questions!")
    qs = get_questions()
    render(qs).run()