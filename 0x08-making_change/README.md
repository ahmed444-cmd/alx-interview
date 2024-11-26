# 0x08. Making Change

## Overview
This project involves solving the "Making Change" problem, which calculates the fewest coins needed to meet a specific total amount, given a set of coin denominations.

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on **Ubuntu 14.04 LTS** using Python 3 (version 3.4.3).
- All files should end with a **new line**.
- The first line of all files must be:
  ```python
  #!/usr/bin/python3
  ```
- A `README.md` file is mandatory in the root of the project folder.
- Code must follow **PEP 8** style guidelines (version 1.7.x).
- All files must be executable.

---

## Task

### **0. Change comes from within**  
**Mandatory**

Write a function to determine the fewest number of coins needed to meet a given amount total.

#### Prototype:
```python
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a total.
    """
```

#### Requirements:
- **Input:**
  - `coins`: A list of integers representing coin denominations (values greater than 0).
  - `total`: An integer representing the total amount.
- **Output:**
  - Return the fewest number of coins needed to meet the total.
  - If the total is `0` or less, return `0`.
  - If the total cannot be met with the given coins, return `-1`.
- You can assume an infinite supply of each coin denomination.
- Your solution's runtime will be evaluated.

---

## Example

### Code (`0-main.py`):
```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Expected output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
```

### Output:
```bash
$ ./0-main.py
7
-1
```

---

## Repository Structure
- **GitHub Repository**: `alx-interview`
- **Directory**: `0x08-making_change`
- **File**: `0-making_change.py`
