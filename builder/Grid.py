import pygame


class Grid:
    width = 0
    height = 0
    col_width = 0
    row_height = 0
    line_color = (50, 50, 50)
    cells_occupied: list[list[bool]] = []

    cols = 0
    rows = 0

    def __init__(self, width, height, col_width, row_height):
        self.width = width
        self.height = height
        self.col_width = col_width
        self.row_height = row_height

        self.cells_occupied = [
            [False for _ in range(height // row_height)]
            for _ in range(width // col_width)
        ]

        self.cols = width // col_width
        self.rows = height // row_height

    def draw(self, screen):
        for x in range(0, self.width, self.col_width):
            pygame.draw.line(screen, self.line_color, (x, 0), (x, self.height))
        for y in range(0, self.height, self.row_height):
            pygame.draw.line(screen, self.line_color, (0, y), (self.width, y))
        pygame.draw.line(
            screen, self.line_color, (self.width, 0), (self.width, self.height)
        )
        pygame.draw.line(
            screen, self.line_color, (0, self.height), (self.width, self.height)
        )

    def get_col_for_x(self, x):
        return x // self.col_width

    def get_row_for_y(self, y):
        return y // self.row_height

    def is_occupied(self, col, row):
        if col < 0 or row < 0:
            return True
        if col >= len(self.cells_occupied):
            return True
        if row >= len(self.cells_occupied[col]):
            return True
        return self.cells_occupied[col][row]

    def set_occupied(self, col, row, value: bool):
        if col < 0 or row < 0:
            return
        if col >= len(self.cells_occupied):
            return
        if row >= len(self.cells_occupied[col]):
            return
        self.cells_occupied[col][row] = value
