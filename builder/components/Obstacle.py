import pygame


class Obstacle:
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen, grid):
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (
                self.x * grid.col_width,
                self.y * grid.row_height,
                self.width * grid.col_width,
                self.height * grid.row_height,
            ),
        )

    def __str__(self):
        return f"Obstacle({self.points})"

    def __repr__(self):
        return str(self)
