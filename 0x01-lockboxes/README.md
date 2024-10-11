# Lockboxes Problem - README

## Overview

This project involves solving the **Lockboxes Problem**, where you have `n` number of locked boxes, each containing keys that may unlock other boxes. The challenge is to determine if **all the boxes** can be opened, starting with the first box, which is unlocked by default.

### Problem Statement

You are given `n` boxes numbered sequentially from `0` to `n-1`. Each box contains a list of keys. A key with the same number as a box can open that box. The first box (`boxes[0]`) is unlocked, and you must determine whether all other boxes can be unlocked using the keys found in the boxes.

### Prototype

```python
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    - boxes (List of Lists): Each index of the list represents a box, 
      and the sublist contains the keys for other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
```

### Input Format

- `boxes` is a list of lists, where each inner list represents the keys found in that particular box.
- A key `k` in `boxes[i]` opens the box numbered `k`.
- Keys are positive integers.
- Box `0` is always unlocked at the start.

### Output

- Return `True` if all boxes can be opened.
- Return `False` if there are some boxes that cannot be opened.

### Example Test Cases

1. **Test Case 1**:
    ```python
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True
    ```
   - Here, each box contains the key to the next box in sequence, and you can open all boxes.

2. **Test Case 2**:
    ```python
    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True
    ```
   - In this case, even though some keys may not correspond to existing boxes, all boxes can be unlocked using the available keys.

3. **Test Case 3**:
    ```python
    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
    ```
   - Not all boxes can be unlocked in this case due to missing keys.

### Approach

The solution to this problem uses **Depth-First Search (DFS)** to simulate the unlocking process:

1. **Start with the first box unlocked**: Since the first box (`boxes[0]`) is always unlocked, begin by collecting its keys.
2. **Track visited boxes**: Keep a set to store which boxes have been unlocked.
3. **Explore all keys**: Use a stack to store keys you discover. As you retrieve keys from a box, unlock the corresponding boxes and add any new keys you find to the stack.
4. **Check if all boxes are unlocked**: If you manage to unlock all boxes, return `True`. If some boxes remain locked, return `False`.

### Solution Implementation

```python
def canUnlockAll(boxes):
    # Start with the first box unlocked
    unlocked_boxes = set([0])
    keys = [0]  # Start DFS from box 0
    
    while keys:
        current_key = keys.pop()  # Get a box key (DFS)
        for key in boxes[current_key]:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.add(key)
                keys.append(key)  # Add new keys to explore
            
    # Check if all boxes are unlocked
    return len(unlocked_boxes) == len(boxes)
```

### Time Complexity

- **O(n + k)**, where `n` is the number of boxes and `k` is the total number of keys. Each box and key is processed at most once.

---

### Conclusion

This project showcases the implementation of a simple algorithmic solution to determine if all boxes in a collection can be unlocked. By using DFS and leveraging a stack-based approach, we can efficiently explore all reachable boxes and determine whether any remain inaccessible.


