import random


def generate_random_ghosts(
    rows,
    cols,
    start,
    end,
    obstacle_probability=0.3
):

    ghosts = []

    for i in range(rows):

        for j in range(cols):

            # Do not block start/end
            if (i, j) == start or (i, j) == end:
                continue

            # Random obstacle generation
            if random.random() < obstacle_probability:

                ghosts.append((i, j))

    return ghosts