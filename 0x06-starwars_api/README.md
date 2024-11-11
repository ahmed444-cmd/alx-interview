Here’s the README content for **0x06. Star Wars API** project, with authorship information removed and additional links omitted:

---

## 0x06. Star Wars API

### Project Overview 🪐
In this project, you will interact with the Star Wars API to retrieve and display data. The focus is on using JavaScript and the `request` module to perform HTTP requests and handle API data.

### Requirements
- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 14.04 LTS using Node.js version 10.14.x
- **File Requirements**:
  - Files must end with a new line.
  - The first line of all files should be `#!/usr/bin/node`.
  - Code should comply with `semistandard` (AirBnB style guide with semicolons).
  - Files must be executable.
  - You are not allowed to use `var`.
- **Readme**: A `README.md` file at the root of the project directory is mandatory.

### Setup Instructions
1. **Install Node 10**:
   ```bash
   curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. **Install `semistandard` for code styling**:
   ```bash
   sudo npm install semistandard --global
   ```

3. **Install the `request` module**:
   ```bash
   sudo npm install request --global
   export NODE_PATH=/usr/lib/node_modules
   ```

### Task Details

#### Task 0: Star Wars Characters
- **Objective**: Write a script that prints all characters of a specified Star Wars movie.
- **Usage**: 
  - The first positional argument is the Movie ID (e.g., `3` for "Return of the Jedi").
  - Display each character's name on a new line in the same order as the “characters” list in the `/films/` endpoint.
  - You must use the Star Wars API and the `request` module.

**Example**:
```bash
./0-starwars_characters.js 3
```
Expected output:
```
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

### Repository Structure
- **GitHub repository**: `alx-interview`
- **Project directory**: `0x06-starwars_api`
- **File**: `0-starwars_characters.js`
