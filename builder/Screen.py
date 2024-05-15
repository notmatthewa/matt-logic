import pygame


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def clear(self):
        self.screen.fill((0, 0, 0))

    def draw_blit(self, x, y, width, height, img):
        self.screen.blit(img, (x, y, width, height))

    def get(self):
        pygame.display.flip()

    def size(self):
        print(self.width, self.height)
