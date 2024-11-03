# UTF-8 Validation Project

**Algorithm** | **Python**

---

### Overview

This project focuses on validating UTF-8 encoding using Python. UTF-8 is a variable-width character encoding used for electronic communication. A properly implemented UTF-8 encoder can ensure that data is accurately interpreted across various systems.

### Resources

For additional context and understanding, consider the following resources:

- [UTF-8 Basics](https://alx-intranet.hbtn.io/rltoken/oqFi6P1hNvp9aSuNv---IQ)
- [Understanding Unicode](https://alx-intranet.hbtn.io/rltoken/d--jVK8sBSlhkosu7pFzdw)

### Project Requirements

- **Text Editors**: `vi`, `vim`, `emacs` are allowed.
- **Environment**: Code should run in an Ubuntu 14.04 LTS environment, using Python 3.4.3.
- **File Conventions**:
  - Each file must end with a new line.
  - The first line of every file should be `#!/usr/bin/python3`.
  - A `README.md` file at the project root is required.
- **Code Standards**: Follow PEP 8 style (version 1.7.x).
- **Permissions**: All files should be executable.

---

## Task Description

### Task 0: UTF-8 Encoding Validation

**Objective**: Create a method to check if a given data list represents valid UTF-8 encoding.

#### Specifications

- **Function Prototype**: `def validUTF8(data)`
- **Returns**: `True` if the data set represents valid UTF-8 encoding, otherwise `False`.
- **Encoding Details**:
  - UTF-8 characters range from 1 to 4 bytes.
  - The input list (`data`) may contain multiple characters.
  - Each integer in the list represents a byte; hence, only the 8 least significant bits of each integer need consideration.

#### Example

```python
#!/usr/bin/python3
"""
Sample test cases
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

---

### Repository Information

- **Repository**: `alx-interview`
- **Directory**: `0x04-utf8_validation`
- **Filename**: `0-validate_utf8.py`

This project will test your ability to apply encoding validation concepts using Python, a crucial skill in data processing and communication.
