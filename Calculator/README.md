**TASK 1**

# Project Title

A brief description of what this project does and who it's for

# Basic Calculator with GUI

## Overview
This repository contains a simple calculator application built with Python's `tkinter` library. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features
- **Addition, Subtraction, Multiplication, Division**: Perform basic arithmetic operations.
- **Clear Button**: Reset the calculation field.
- **Parentheses**: Use parentheses to group expressions and control the order of operations.
- **Error Handling**: Catch and display errors in the calculation.

## Prerequisites
- Python 3.x

## How to Run
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Isaadqurashi/CodeClause/tree/main/Calculator
   cd isaadqurashi-CodeClause
   ```

2. **Run the Application**:
   ```bash
   python calculator.py
   ```

## Code Explanation
Here's a brief overview of the code structure:

- **Global Variables**:
  - `calculation`: Stores the current calculation as a string.

- **Functions**:
  - `add_to_calculation(symbol)`: Adds a symbol (number or operator) to the calculation.
  - `evaluate_calculation()`: Evaluates the current calculation and displays the result.
  - `clear_field()`: Clears the current calculation.

- **GUI Setup**:
  - The `tkinter` library is used to create the GUI.
  - The main window is created with `root = tk.Tk()`.
  - Buttons are created for numbers (0-9), operators (+, -, *, /), parentheses, clear, and equals.
  - The `text_result` widget displays the current calculation and result.

## File Structure
```
CodeClause/
│
├── README.md
└── calculator.py
```

## Example
![Calculator GUI](https://i.ibb.co/9WfyJrb/Screenshot-2024-07-27-085038.png")

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.

---

