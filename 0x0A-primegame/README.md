# 0x09. Prime Game

## 📖 Overview
This project explores the **Prime Game**, a problem-solving challenge where two players, Maria and Ben, take turns removing prime numbers and their multiples from a set of integers. The player who cannot make a move loses the round.

---

## 📃 Topics Covered
- Prime number concepts
- Algorithmic problem-solving
- Optimal strategies for game theory

---

## 💻 Task: Prime Game

### Description
Maria and Ben play `x` rounds of a game. In each round, they start with a set of consecutive integers from `1` to `n`:
1. Maria goes first, and players take turns picking a prime number from the set.
2. The selected prime and its multiples are removed from the set.
3. A player loses when no moves are possible.

### Prototype
```python
def isWinner(x, nums):
    """
    Determines the winner of the Prime Game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the value of n for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben").
        None: If the winner cannot be determined.
    """
```

### Requirements
- **Input:**
  - `x`: The number of rounds.
  - `nums`: A list of integers, where each integer represents `n` for a round.
- **Output:**
  - Return the name of the player who wins the most rounds:
    - `"Maria"` if Maria wins the most.
    - `"Ben"` if Ben wins the most.
    - Return `None` if there's a tie or no clear winner.
- Constraints:
  - `x` and the maximum value of `nums` will not exceed `10,000`.
  - No external libraries or packages can be used.

---

## 💡 Example

```python
x = 3
nums = [4, 5, 1]

# Round 1: n = 4
# Maria picks 2 (removes 2, 4). Ben picks 3 (removes 3). Ben wins.

# Round 2: n = 5
# Maria picks 2 (removes 2, 4). Ben picks 3 (removes 3). Maria picks 5 (removes 5). Maria wins.

# Round 3: n = 1
# No prime numbers for Maria to choose. Ben wins.

# Result: Ben wins 2 rounds, Maria wins 1 round. Ben is the overall winner.
```

### Sample Output
```bash
$ cat main_0.py
#!/usr/bin/python3
isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

$ ./main_0.py
Winner: Ben
```

---

## 🛠️ Task Setup
### Solution File
1. Create the solution file:
   ```bash
   touch 0-prime_game.py
   chmod +x 0-prime_game.py
   ```

2. Lint your code:
   ```bash
   pep8 0-prime_game.py
   ```

### Test File
1. Create a test file:
   ```bash
   touch 0-main.py
   chmod +x 0-main.py
   ```

2. Run the test:
   ```bash
   ./0-main.py
   ```

---

## 🔧 Repository Structure
- **GitHub Repository**: `alx-interview`
- **Directory**: `0x0A-primegame`
- **File**: `0-prime_game.py`

--- 
