from datetime import datetime

import pygame

from UI.color_wheel import ColorWheel
from builder.Screen import Screen
from builder.Grid import Grid
from builder.components.Line import Line
from builder.components.Obstacle import Obstacle

running = True

WIDTH = 1200
HEIGHT = 800

screen = Screen(WIDTH + 1, HEIGHT + 1)
grid = Grid(WIDTH, HEIGHT, 10, 10)

start_point = (0, 0)
currently_solving = False
currently_drawing = False

color_wheel = ColorWheel()
color_wheel_display_time = 2
color_wheel_showing = False
color_wheel_started_showing = datetime.min

line_size = 1
line_size_display_time = 2
line_size_showing = False
line_size_started_showing = datetime.min

objs = []


def main():
    run()


def run():
    global running, start_point, currently_solving, currently_drawing, color_wheel_showing
    global color_wheel_started_showing, line_size, line_size_showing, line_size_started_showing

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = grid.get_col_for_x(mouse_x)
                row = grid.get_row_for_y(mouse_y)

                start_point = (col, row)
                currently_solving = True

            if (
                event.type == pygame.MOUSEBUTTONUP
                and event.button == 1
                and currently_solving
            ):
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = min(max(grid.get_col_for_x(mouse_x), 0), grid.cols - 1)
                row = min(max(grid.get_row_for_y(mouse_y), 0), grid.rows - 1)

                end_point = (col, row)
                line = Line(
                    color=color_wheel.get_current_color(), stroke_width=line_size
                )
                line.solve(
                    grid,
                    start_point,
                    end_point,
                    [o.points for o in objs if isinstance(o, Line)],
                )
                if start_point == end_point:
                    currently_solving = False
                    continue

                if len(line.points) < 2:
                    currently_solving = False
                    continue

                line.draw(screen.screen, grid)
                screen.get()

                objs.append(line)

                currently_solving = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                # delete if on line
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = min(max(grid.get_col_for_x(mouse_x), 0), grid.cols - 1)
                row = min(max(grid.get_row_for_y(mouse_y), 0), grid.rows - 1)

                for obj in objs:
                    if isinstance(obj, Line):
                        for point in obj.points:
                            if point[0] == col and point[1] == row:
                                objs.remove(obj)
                                break

            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                currently_solving = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                currently_drawing = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 2:
                currently_drawing = False

            if event.type == pygame.MOUSEWHEEL:
                if pygame.key.get_pressed()[pygame.K_LCTRL]:
                    line_size = min(max(line_size + (event.y * 2), 1), 5)
                    line_size_showing = True
                    line_size_started_showing = datetime.now()

                    color_wheel_showing = False
                else:
                    if event.y > 0:
                        color_wheel_showing = True
                        color_wheel_started_showing = datetime.now()
                        color_wheel.next_color()
                    else:
                        color_wheel_showing = True
                        color_wheel_started_showing = datetime.now()
                        color_wheel.previous_color()

                    line_size_showing = False

        if currently_drawing:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = min(max(grid.get_col_for_x(mouse_x), 0), grid.cols - 1)
            row = min(max(grid.get_row_for_y(mouse_y), 0), grid.rows - 1)

            obs = Obstacle(col - 2, row - 2, 4, 4)
            obs.draw(screen.screen, grid)
            objs.append(obs)

            top_left = (col - 2, row - 2)

            for i in range(4):
                for j in range(4):
                    grid.set_occupied(top_left[0] + i, top_left[1] + j, True)

        screen.clear()

        grid.draw(screen.screen)

        for obj in objs:
            obj.draw(screen.screen, grid)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        col = min(max(grid.get_col_for_x(mouse_x), 0), grid.cols - 1)
        row = min(max(grid.get_row_for_y(mouse_y), 0), grid.rows - 1)

        if currently_solving:
            solve_ghost = Line(
                stroke_width=line_size,
                color=tuple(
                    map(
                        lambda x: max(x - 150, 0), list(color_wheel.get_current_color())
                    )
                ),
            )
            solve_ghost.solve(
                grid,
                start_point,
                (col, row),
                [o.points for o in objs if isinstance(o, Line)],
            )
            solve_ghost.draw(screen.screen, grid)

        if color_wheel_showing:
            if (
                datetime.now() - color_wheel_started_showing
            ).seconds > color_wheel_display_time:
                color_wheel_showing = False
            mouse_x, mouse_y = pygame.mouse.get_pos()
            color_wheel.draw(screen.screen, mouse_x + 50, mouse_y, 25)

        if line_size_showing:
            if (
                datetime.now() - line_size_started_showing
            ).seconds > line_size_display_time:
                line_size_showing = False
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pygame.draw.rect(
                screen.screen,
                (255, 255, 255),
                (mouse_x + 50, mouse_y - int(line_size / 2), 10, line_size),
            )
            pygame.draw.circle(
                screen.screen,
                (255, 255, 255),
                (mouse_x + 50, mouse_y),
                int(line_size / 2),
            )
            pygame.draw.circle(
                screen.screen,
                (255, 255, 255),
                (mouse_x + 60, mouse_y),
                int(line_size / 2),
            )

        pygame.draw.rect(screen.screen, (255, 0, 0), (col * 10, row * 10, 10, 10))

        screen.get()

    pygame.quit()


if __name__ == "__main__":
    main()
