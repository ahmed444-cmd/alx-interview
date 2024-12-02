# Island Perimeter

## Overview
This project involves solving a coding challenge to determine the perimeter of an island represented in a grid. The grid is a 2D list where land and water are represented by `1` and `0`, respectively.

---

## Task

### **0. Island Perimeter**

Write a function to calculate the perimeter of the island described in the grid.

#### Prototype:
```python
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.
    """
```

#### Requirements:
- **Input:**
  - `grid`: A list of lists of integers where:
    - `0` represents water.
    - `1` represents land.
  - Each cell is a square with a side length of 1.
  - Cells are connected **horizontally** or **vertically** (not diagonally).
  - The grid is rectangular, with a width and height not exceeding 100.
- **Output:**
  - Return an integer representing the perimeter of the island.
- The grid will be surrounded by water.
- There is only one island (or none).
- The island will not contain "lakes" (water inside the island).

---

## Example

### Code:
```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Expected output: 16
```

---

## Repository Structure
- **File**: `0-island_perimeter.py`  
- **Function**: `island_perimeter(grid)`  

---
