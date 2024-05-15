import pygame

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

objs = []


def main():
    run()


def run():
    global running, start_point, currently_solving, currently_drawing

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

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = min(max(grid.get_col_for_x(mouse_x), 0), grid.cols - 1)
                row = min(max(grid.get_row_for_y(mouse_y), 0), grid.rows - 1)

                end_point = (col, row)
                line = Line()
                line.solve(
                    grid,
                    start_point,
                    end_point,
                    [o.points for o in objs if isinstance(o, Line)],
                )
                line.draw(screen.screen, grid)
                screen.get()

                objs.append(line)
                print(len(objs))

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

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                currently_drawing = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 2:
                currently_drawing = False

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
            solve_ghost = Line(color=(100, 100, 100))
            solve_ghost.solve(
                grid,
                start_point,
                (col, row),
                [o.points for o in objs if isinstance(o, Line)],
            )
            solve_ghost.draw(screen.screen, grid)

        pygame.draw.rect(screen.screen, (255, 0, 0), (col * 10, row * 10, 10, 10))

        screen.get()

    pygame.quit()


if __name__ == "__main__":
    main()
