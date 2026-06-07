from collections import deque
from maze import *
from exception import *

class BFSPacMan:

    def __init__(self, grid: Maze) -> None:
        self.navigator_maze = grid.grid_representation

    def find_shortest_path(self, start: tuple, end: tuple) -> list:

        rows = len(self.navigator_maze)
        cols = len(self.navigator_maze[0])

        # Directions: Down, Up, Right, Left
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # Queue stores:
        # ((current_x, current_y), path_so_far)
        queue = deque()

        queue.append((start, [start]))

        # Visited cells
        visited = set()

        visited.add(start)

        while queue:

            current, path = queue.popleft()

            # Destination reached
            if current == end:
                return path

            # Explore neighbours
            for dx, dy in directions:

                new_x = current[0] + dx
                new_y = current[1] + dy

                # Valid move check
                if (
                    0 <= new_x < rows and
                    0 <= new_y < cols and
                    self.navigator_maze[new_x][new_y] == 0 and
                    (new_x, new_y) not in visited
                ):

                    visited.add((new_x, new_y))

                    new_path = path + [(new_x, new_y)]

                    queue.append(
                        (
                            (new_x, new_y),
                            new_path
                        )
                    )

        # No path found
        raise PathNotFoundException()