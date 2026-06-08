from navigator import *
from bfs_navigator import *
from maze import *
from maze_generator import *
from visualizer import *

import time


def is_valid(x: int, y: int, rows: int, cols: int) -> bool:

    return (
        0 <= x < rows and
        0 <= y < cols
    )


def is_neighbour(
    x1: int,
    y1: int,
    x2: int,
    y2: int
) -> bool:

    return abs(x2 - x1) + abs(y2 - y1) == 1


if __name__ == "__main__":

    # GRID SIZE
    grid_rows = 8
    grid_cols = 8

    # START AND END
    start_point = (0, 0)
    end_point = (7, 7)

    # RANDOM OBSTACLES
    ghosts = generate_random_ghosts(
        grid_rows,
        grid_cols,
        start_point,
        end_point,
        obstacle_probability=0.28
    )

    # CREATE MAZE
    sample_grid = Maze(grid_rows, grid_cols)

    for ghost in ghosts:
        sample_grid.add_ghost(
            ghost[0],
            ghost[1]
        )

    print("\nGenerated Maze:\n")

    sample_grid.print_grid()

    try:

        # ---------------- DFS ----------------
        dfs_grid = Maze(grid_rows, grid_cols)

        for ghost in ghosts:
            dfs_grid.add_ghost(
                ghost[0],
                ghost[1]
            )

        PacManInstance = PacMan(dfs_grid)

        dfs_start = time.time()

        dfs_path = PacManInstance.find_path(
            start_point,
            end_point
        )

        dfs_end = time.time()

        print("\nDFS Path:")
        print(dfs_path)

        print("DFS Path Length:", len(dfs_path))

        print(
            "DFS Execution Time:",
            round(dfs_end - dfs_start, 6),
            "seconds"
        )

        # ---------------- BFS ----------------
        bfs_grid = Maze(grid_rows, grid_cols)

        for ghost in ghosts:
            bfs_grid.add_ghost(
                ghost[0],
                ghost[1]
            )

        BFSInstance = BFSPacMan(bfs_grid)

        bfs_start = time.time()

        shortest_path = BFSInstance.find_shortest_path(
            start_point,
            end_point
        )

        bfs_end = time.time()

        print("\nBFS Shortest Path:")
        print(shortest_path)

        print("BFS Path Length:", len(shortest_path))

        print(
            "BFS Execution Time:",
            round(bfs_end - bfs_start, 6),
            "seconds"
        )

        print(
            "\nBFS guarantees the shortest path "
            "in an unweighted maze."
        )

        # VISUALIZATION
        visualize_maze(
            bfs_grid.grid_representation,
            shortest_path,
            start_point,
            end_point
        )

    except PathNotFoundException:

        print(
            "\nNo valid path exists "
            "between start and end points."
        )

    except Exception as error:

        print("\nUnexpected Error:")
        print(error)