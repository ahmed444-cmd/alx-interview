# 0x03. Log Parsing

## Table of Contents
- Overview
- Key Concepts
- Resources
- Requirements
- Task Description

## Overview
In this project, "0x03. Log Parsing," you'll leverage your Python skills to parse and process real-time data streams. The project focuses on reading data from standard input (stdin), parsing log entries, and performing calculations based on specific input formats. This exercise is designed to deepen your understanding of data processing in Python, particularly in a real-time context.

## Key Concepts
The following concepts are essential to successfully complete this project:

### File I/O in Python
- Learn how to read from `sys.stdin` line by line.
- [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

### Signal Handling in Python
- Handle keyboard interruptions (CTRL + C) using Python’s signal handling.
- [Python Signal Handling](https://docs.python.org/3/library/signal.html)

### Data Processing
- Parse strings to extract relevant data.
- Aggregate data to compute summaries.

### Regular Expressions
- Validate the format of each line using regular expressions.
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)

### Dictionaries in Python
- Use dictionaries to count occurrences of status codes and track file sizes.
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### Exception Handling
- Manage exceptions during file reading and data processing.
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

## Resources
- Mock Technical Interview

## Requirements
- Editors: `vi`, `vim`, `emacs`
- Python version: 3.4.3, executed on Ubuntu 20.04 LTS.
- Each file must end with a new line.
- The first line of every file should be `#!/usr/bin/python3`.
- A `README.md` file at the root of the project directory is mandatory.
- Your code should follow PEP 8 style (version 1.7.x).
- All files must be executable.
- File lengths will be tested using `wc`.

## Task Description

### 0. Log Parsing
Write a Python script that reads from standard input (stdin) and computes the following metrics:

#### Input Format:
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```
- If the input does not match this format, skip the line.

#### Output:
- After every 10 lines or after a keyboard interruption (CTRL + C), print:
  - **Total file size:** Sum of all `<file size>` values from the input.
  - **Number of lines per status code:** Print the number of times each status code appears in ascending order.
    - Status codes to track: 200, 301, 400, 401, 403, 404, 405, 500.
    - If a status code does not appear, do not include it in the output.

#### Example:
```bash
$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```

In case of a keyboard interruption (CTRL + C), the script should print the current statistics before exiting:
```bash
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

## Example Code

### Log Generator (`0-generator.py`):
```python
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
```

### Log Stats (`0-stats.py`):
```python
#!/usr/bin/python3
import sys

# Your log parsing logic here
```
