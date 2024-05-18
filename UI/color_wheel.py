import pygame


class ColorWheel:
    possible_colors = [
        (255, 255, 255),
        (255, 0, 0),
        (255, 255, 0),
        (0, 255, 0),
        (0, 255, 255),
        (0, 0, 255),
        (255, 0, 255),
    ]
    current_color_index = 0

    def next_color(self):
        self.current_color_index = (self.current_color_index + 1) % (
            len(self.possible_colors) - 1
        )

    def previous_color(self):
        self.current_color_index = (self.current_color_index - 1) % (
            len(self.possible_colors) - 1
        )
        if self.current_color_index < 0:
            self.current_color_index = len(self.possible_colors) - 1

    def get_current_color(self):
        return self.possible_colors[self.current_color_index]

    def get_previous_color(self):
        return self.possible_colors[
            (self.current_color_index - 1) % (len(self.possible_colors) - 1)
        ]

    def get_next_color(self):
        return self.possible_colors[
            (self.current_color_index + 1) % (len(self.possible_colors) - 1)
        ]

    def draw(self, screen, x, y, radius):
        margin = radius * 2 + 10

        pygame.draw.circle(screen, self.get_current_color(), (x, y), radius)
        pygame.draw.circle(
            screen, self.get_previous_color(), (x, y - margin), int(radius * 0.75)
        )
        pygame.draw.circle(
            screen, self.get_next_color(), (x, y + margin), int(radius * 0.75)
        )

        pygame.draw.circle(screen, (255, 255, 255), (x, y), radius + 1, 2)
        pygame.draw.circle(
            screen, (255, 255, 255), (x, y - margin), int(radius * 0.75) + 1, 2
        )
        pygame.draw.circle(
            screen, (255, 255, 255), (x, y + margin), int(radius * 0.75) + 1, 2
        )
