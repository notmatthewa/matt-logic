import pygame

from builder.Grid import Grid


class Line:
    points = []
    color = (255, 255, 255)

    def __init__(self, points=None, color=(255, 255, 255)):
        if points is None:
            points = []

        self.points = points
        self.color = color

    def draw(self, screen, grid: Grid):
        for i in range(len(self.points) - 1):
            pygame.draw.line(
                screen,
                self.color,
                (
                    self.points[i][0] * grid.col_width + grid.col_width // 2,
                    self.points[i][1] * grid.row_height + grid.row_height // 2,
                ),
                (
                    self.points[i + 1][0] * grid.col_width + grid.col_width // 2,
                    self.points[i + 1][1] * grid.row_height + grid.row_height // 2,
                ),
            )

        start = self.points[0]
        end = self.points[-1]
        pygame.draw.circle(
            screen,
            self.color,
            (
                start[0] * grid.col_width + grid.col_width // 2,
                start[1] * grid.row_height + grid.row_height // 2,
            ),
            3,
        )

        pygame.draw.circle(
            screen,
            self.color,
            (
                end[0] * grid.col_width + grid.col_width // 2,
                end[1] * grid.row_height + grid.row_height // 2,
            ),
            3,
        )

    def add_point(self, x, y):
        self.points.append((x, y))

    def remove_point(self, x, y):
        self.points.remove((x, y))

    from collections import deque

    def solve(
        self,
        grid: Grid,
        start: tuple[int, int],
        end: tuple[int, int],
        existing_lines: list[tuple[int, int]],
    ):
        """
        Solve the line from start to end in the fewest amount of points using only 90-degree turns.
        """
        self.points = []

        # Directions: (dx, dy, turn direction) where turn direction is 0 for no turn, 1 for horizontal, 2 for vertical
        directions = [(1, 0, 1), (-1, 0, 1), (0, 1, 2), (0, -1, 2)]

        # BFS queue: stores tuples of (current position, path taken, last direction)
        queue = [(start, [start], None)]
        visited = set()
        visited.add(start)

        while queue:
            current, path, last_direction = queue.pop(0)
            x, y = current

            if current == end:
                self.points = path
                return

            for dx, dy, direction in directions:
                next_pos = (x + dx, y + dy)
                if next_pos in visited:
                    continue
                if (
                    grid.is_occupied(next_pos[0], next_pos[1])
                    or next_pos in existing_lines
                ):
                    continue

                if last_direction is None or last_direction == direction:
                    next_path = path + [next_pos]
                else:
                    next_path = path + [current, next_pos]

                queue.append((next_pos, next_path, direction))
                visited.add(next_pos)

        # If no path found
        print("No path found or endpoint inside obstacle")
        self.points.append(end)

        return self.points if start != end else None
