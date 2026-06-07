import pygame
import time


# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


CELL_SIZE = 60


def draw_grid(screen, grid, path, start, end):

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):

        for j in range(cols):

            rect = pygame.Rect(
                j * CELL_SIZE,
                i * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            # WALL / GHOST
            if grid[i][j] == 1:
                pygame.draw.rect(screen, BLACK, rect)

            # NORMAL CELL
            else:
                pygame.draw.rect(screen, WHITE, rect)

            # DRAW BORDER
            pygame.draw.rect(screen, BLUE, rect, 2)

    # DRAW PATH
    for cell in path:

        rect = pygame.Rect(
            cell[1] * CELL_SIZE,
            cell[0] * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )

        pygame.draw.rect(screen, GREEN, rect)

        pygame.draw.rect(screen, BLUE, rect, 2)

        pygame.display.update()

        time.sleep(0.08)

    # START CELL
    start_rect = pygame.Rect(
        start[1] * CELL_SIZE,
        start[0] * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE
    )

    pygame.draw.rect(screen, GREEN, start_rect)

    # END CELL
    end_rect = pygame.Rect(
        end[1] * CELL_SIZE,
        end[0] * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE
    )

    pygame.draw.rect(screen, RED, end_rect)


def visualize_maze(grid, path, start, end):

    pygame.init()

    rows = len(grid)
    cols = len(grid[0])

    width = cols * CELL_SIZE
    height = rows * CELL_SIZE

    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Maze Solver Visualization")

    running = True

    while running:

        screen.fill(WHITE)

        draw_grid(
            screen,
            grid,
            path,
            start,
            end
        )

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

    pygame.quit()