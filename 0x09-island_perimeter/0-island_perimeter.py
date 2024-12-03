#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A 2D list where 0 represents water
                                    and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Add 4 for the land cell
                perimeter += 4

                # Check for adjacent land cells to subtract shared edges
                if r > 0 and grid[r - 1][c] == 1:  # Cell above
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # Cell to the left
                    perimeter -= 2

    return perimeter
