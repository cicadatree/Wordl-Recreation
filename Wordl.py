import pygame
import random

class Wordle:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.word_list = ['apple', 'grape', 'berry', 'melon', 'lemon']
        self.target_word = random.choice(self.word_list)
        self.font = pygame.font.Font(None, 36)

        self.guesses = []
        self.MAX_GUESSES = 6
        self.input_text = ''

    def run_game(self):
        running = True
        while running:
            self.screen.fill((255, 255, 255))  # Fill the screen with white
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(self.guesses) < self.MAX_GUESSES:
                        guess = self.input_text
                        if len(guess) == 5:
                            self.guesses.append(guess)
                            self.input_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        if len(self.input_text) < 5:
                            self.input_text += event.unicode

            y = 50
            for guess in self.guesses:
                color_boxes = self.color_boxes(guess)
                for i, box in enumerate(color_boxes):
                    pygame.draw.rect(self.screen, box[1], (50 + 60 * i, y, 50, 50))
                    text = self.font.render(box[0], True, (0, 0, 0))
                    text_rect = text.get_rect(center=(50 + 60 * i + 25, y + 25))  # This line is changed
                    self.screen.blit(text, text_rect)
                y += 60

            # Render the input text
            text_surface = self.font.render(self.input_text, True, (0, 0, 0))
            self.screen.blit(text_surface, (50, self.WINDOW_HEIGHT - 50))

            # Render the instructions
            instruction_text = 'Guess a 5-letter word. Press ENTER to submit your guess.'
            instruction_surface = self.font.render(instruction_text, True, (0, 0, 0))
            self.screen.blit(instruction_surface, (50, 20))

            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()

    def color_boxes(self, guess):
        color_boxes = []
        for i in range(5):
            if guess[i] == self.target_word[i]:
                color_boxes.append((guess[i], (0, 255, 0)))
            elif guess[i] in self.target_word:
                color_boxes.append((guess[i], (255, 255, 0)))
            else:
                color_boxes.append((guess[i], (255, 0, 0)))
        return color_boxes


if __name__ == "__main__":
    wordle_game = Wordle()
    wordle_game.run_game()
