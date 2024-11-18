
# 0x07. Rotate 2D Matrix

## Overview
This project focuses on implementing a function to rotate a 2D matrix 90 degrees clockwise **in-place**. The function modifies the matrix directly without creating a new matrix.

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using Python 3 (version 3.8.10).
- All files must end with a **new line**.
- The first line of all files must be:
  ```python
  #!/usr/bin/python3
  ```
- A `README.md` file is mandatory in the root of the project folder.
- Code must follow the **pycodestyle** style guide (version 2.8.0).
- No external modules may be imported.
- All modules and functions must include documentation.
- All files must be executable.

---

## Task

### **0. Rotate 2D Matrix**  
**Mandatory**

Write a function to rotate an `n x n` 2D matrix 90 degrees clockwise.

#### Prototype:
```python
def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.
    """
```

#### Requirements:
- The function should not return anything; the input matrix must be updated in-place.
- The input matrix will always be non-empty and have two dimensions.

---

## Example

### Code (`main_0.py`):
```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

### Output:
```bash
$ ./main_0.py
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

---

## Repository Structure
- **GitHub Repository**: `alx-interview`
- **Directory**: `0x07-rotate_2d_matrix`
- **File**: `0-rotate_2d_matrix.py`
