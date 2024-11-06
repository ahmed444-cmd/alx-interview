# N Queens Puzzle

## Overview
The N Queens puzzle challenges you to place `N` queens on an `NxN` chessboard such that no two queens can attack each other. This means each queen must be positioned on a unique row, column, and diagonal.

Since queens can move any number of squares vertically, horizontally, or diagonally, the solution requires strategic placement to avoid conflicts. This puzzle is most efficiently solved using a backtracking algorithm.

### About Backtracking
Backtracking is an algorithmic technique that incrementally builds solutions and abandons paths that can’t lead to a complete, valid solution. In this puzzle, backtracking helps to explore possible queen placements and backtrack as soon as conflicts are detected.

## Usage
Run the program as follows:
```
nqueens N
```
where `N` is the number of queens to place on the board. Ensure that:
- `N` is an integer greater than or equal to 4.

The program will output all possible solutions in the following format:

```bash
$ ./0-nqueens 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

Each inner list represents the coordinates `[row, column]` of a queen on the `NxN` chessboard.
