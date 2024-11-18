Here's the updated `README.md` reflecting your renamed files:

---

# Ranking Algorithm

A Python application to calculate and display the ranking table for a league based on match results. It supports input via a file or standard input (stdin).

---

## Features

- Calculates rankings based on match results.
- Supports both file input and stdin.
- Produces rankings ordered by points (and alphabetically in case of ties).
- Includes a comprehensive suite of tests.

---

## Requirements

- Python 3.6 or higher

---

## Installation

1. Clone this repository or download the project files.
2. Navigate to the project directory in your terminal.

---

## Usage

### Running the Code

You can provide match results either through a file or stdin.

#### Input via File

1. Create a text file containing match results, e.g., `test1.txt`:

   ```
   Lions 3, Snakes 3
   Tarantulas 1, FC Awesome 0
   Lions 1, FC Awesome 1
   Tarantulas 3, Snakes 1
   Lions 4, Grouches 0
   ```

2. Run the application by specifying the file:

   ```bash
   python3 ranking.py test1.txt
   ```

#### Input via Stdin

You can also provide input directly through stdin:

```bash
echo -e "Lions 3, Snakes 3\nTarantulas 1, FC Awesome 0\nLions 1, FC Awesome 1\nTarantulas 3, Snakes 1\nLions 4, Grouches 0" | python3 ranking.py
```

---

## Output

The output will be printed to the console in the following format:

```
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```

---

## Testing

The project includes a suite of tests to verify its correctness and robustness.

### Running the Tests

1. Navigate to the project directory.
2. Run the tests using the `unittest` framework:

   ```bash
   python3 -m unittest test_ranking.py
   ```

   This will automatically discover and run all tests in `test_ranking.py`.

### Key Tests

- **Functionality Tests**:
  - Ensure rankings are calculated correctly.
  - Validate handling of ties, alphabetical ordering, and 0-point teams.
- **Input Tests**:
  - Verify correct handling of input via files and stdin.
  - Ensure proper error handling for missing files.

---

## File Structure

- `ranking.py`: The main application script.
- `test_ranking.py`: Unit tests for core functions.
- `test1.txt`: Example input file for testing.
- `README.md`: Documentation for the project.

---
