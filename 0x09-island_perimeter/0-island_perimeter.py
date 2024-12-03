#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    Args:
    grid (list of list of int): 
    A list of list of integers where
    0 represents water and 1 represents land.
    Returns:
    int: The perimeter of the island.
    """
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        sublime_text
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                # Start with a full square (4 sides)
                perimeter += 4
                # Check the cell above
                if r > 0 and grid[r - 1][c] == 1:
                perimeter -= 2
                # Check the cell to the left
                if c > 0 and grid[r][c - 1] == 1:
                perimeter -= 2

return perimeter
