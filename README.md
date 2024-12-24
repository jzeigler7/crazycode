# Crazy Code

## Overview
The OpenAI Crazy Code Script is a Python program designed to automate the process of refactoring Python code using the OpenAI GPT model. It focuses on various refactoring techniques, including renaming identifiers, minimizing local variables, combining lines, and optimizing print statements. The script uses OpenAI's API to perform these tasks dynamically and writes the modified code back to the input file.

## Features
1. **Refactoring Options**:
   - **Minimize Local Variables**: Removes unnecessary local variable assignments by inlining values where possible.
   - **Rename Identifiers**: Ensures variable names are at most 5 characters long and function names are formatted as two words separated by an underscore.
   - **Condense Lines**: Combines consecutive statements into fewer lines, up to two long or three short statements per line.
   - **Optimize `if` Statements**: Moves single statements in `if` blocks onto the same line as the condition if valid.
   - **Lowercase Print Strings**: Converts all string literals passed to `print` functions to lowercase.
   - **Remove Unnecessary Whitespace**: Strips unnecessary whitespace outside of string literals and maintains valid indentation.
   - **Finalize Print Statements**: Simplifies print statements by removing headers or unnecessary labels and retaining only essential information.

2. **Customizable Input**:
   - Accepts user-provided Python files for refactoring.
   - Supports optional custom OpenAI API key files.

3. **Output**:
   - Overwrites the original file with the refactored code.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/openai-refactor-script.git
   cd openai-refactor-script
   ```

2. **Install Dependencies**:
   Install the `openai` library:
   ```bash
   pip install openai
   ```

3. **Setup OpenAI API Key**:
   - Save your OpenAI API key in a file named `openai_key.txt`.
   - Alternatively, specify a custom key file during execution.

## Usage
1. **Run the Script**:
   ```bash
   python crazy_code.py <path_to_python_file> [optional_key_file]
   ```
   - `<path_to_python_file>`: Path to the Python file to be refactored.
   - `[optional_key_file]`: Path to the file containing the OpenAI API key (default: `openai_key.txt`).

2. **Example**:
   ```bash
   python crazy_code.py example.py
   ```

3. **Output**:
   - The original file will be overwritten with the refactored code.

## Key Functions
### **Refactoring Methods**
- **`minimize_local_variables`**:
  Removes redundant local variables, inlining values directly into expressions.
- **`rename_identifiers`**:
  Shortens variable names to 5 characters and enforces function names to have a two-word underscore format.
- **`condense_adjacent_lines`**:
  Combines multiple statements into fewer lines while maintaining functionality.
- **`join_if_statements`**:
  Refactors `if` statements to place simple block statements on the same line as the condition.
- **`enforce_lowercase_prints`**:
  Converts string literals in `print` statements to lowercase.
- **`remove_whitespace_outside_prints`**:
  Eliminates extraneous whitespace while preserving essential indentation.
- **`finalize_prints`**:
  Simplifies print statements by removing unnecessary labels or headers.

### **Helper Functions**
- **`get_openai_api_key`**:
  Reads the OpenAI API key from a specified file.
- **`remove_comments_and_blank_lines`**:
  Strips comments and blank lines from the refactored code.

## Example Workflow
### Input Code:
```python
x = 10
y = 20
if x > y:
    print("PASS: x is greater")
else:
    print("FAIL: y is greater")
```
### Output Code:
```python
if 10 > 20: print("pass: x is greater")
else: print("fail: y is greater")
```

## Error Handling
- **File Validation**:
  Ensures the input file exists and is a valid Python file.
- **API Key Validation**:
  Verifies the existence of the OpenAI API key file.
- **Output Management**:
  Handles exceptions and logs errors if the refactoring process fails.
