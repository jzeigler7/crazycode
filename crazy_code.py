import sys
import os
from openai import OpenAI

def get_openai_api_key(key_file_path: str) -> str:
    if not os.path.exists(key_file_path):
        print(f"Error: OpenAI key file '{key_file_path}' not found.")
        sys.exit(1)
    with open(key_file_path, "r", encoding="utf-8") as key_file:
        return key_file.read().strip()

def minimize_local_variables(code_str: str, client: OpenAI) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a Python code refactoring assistant. "
                "Return ONLY the refactored code with correct Python indentation. "
                "Do not include explanations, comments, code fences, or additional text."
            ),
        },
        {
            "role": "user",
            "content": (
                "Refactor the following Python code so that absolutely no local variable assignments "
                "remain, unless their removal makes it impossible to maintain the same functionality. "
                "This includes lists and other static data structures. "
                "Do not add any explanations or comments. "
                "Do not output anything other than the refactored code. "
                "All local variables that can be removed without breaking the code "
                "must be removed, directly substituting assigned values inline where possible. "
                "It's acceptable if the code becomes slower or more complex. "
                "Preserve correct functionality and indentation.\n\n"
                f"{code_str}"
            ),
        },
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.0,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].message.content

def rename_identifiers(code_str: str, client: OpenAI) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a Python code refactoring assistant. "
                "Return ONLY the refactored code with correct Python indentation. "
                "Do not include explanations, comments, code fences, or additional text."
            ),
        },
        {
            "role": "user",
            "content": (
                "Refactor the following Python code so that all variable names are at most 5 characters long, "
                "and all method/function names consist of exactly two words separated by an underscore. "
                "Do not add any explanations, comments, or additional text. "
                "Do not output anything other than the refactored code. Preserve correct functionality and indentation.\n\n"
                f"{code_str}"
            ),
        },
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.0,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].message.content

def condense_adjacent_lines(code_str: str, client: OpenAI) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a Python code refactoring assistant. "
                "Return ONLY the refactored code with correct Python indentation. "
                "Do not include explanations, comments, code fences, or additional text."
            ),
        },
        {
            "role": "user",
            "content": (
                "Refactor the following Python code by combining consecutive statements into fewer lines. "
                "At most two long statements or three short statements per line are allowed. "
                "Do not add explanations, comments, or additional text. "
                "Do not break functionality. Preserve correct indentation.\n\n"
                f"{code_str}"
            ),
        },
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.0,
        max_tokens=3000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].message.content

def join_if_statements(code_str: str, client: OpenAI) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a Python code refactoring assistant. "
                "Return ONLY the refactored code with correct Python indentation. "
                "Do not include explanations, comments, code fences, or additional text."
            ),
        },
        {
            "role": "user",
            "content": (
                "Refactor the following Python code so that any first statement(s) inside an if block "
                "are placed on the same line as the if statement whenever syntactically valid. "
                "Do not add explanations, comments, or additional text. "
                "Preserve correct functionality and indentation.\n\n"
                f"{code_str}"
            ),
        },
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.0,
        max_tokens=3000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].message.content

def enforce_lowercase_prints(code_str: str, client: OpenAI) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a Python code refactoring assistant. "
                "Return ONLY the refactored code with correct Python indentation. "
                "Do not include explanations, comments, code fences, or additional text."
            ),
        },
        {
            "role": "user",
            "content": (
                "Refactor the following Python code so that any string literals passed to print functions "
                "are converted to all lowercase. Non-string arguments must remain unchanged. "
                "Do not add explanations, comments, or additional text. "
                "Return only the code.\n\n"
                f"{code_str}"
            ),
        },
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.0,
        max_tokens=3000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].message.content

def remove_whitespace_outside_prints(code_str: str, client: OpenAI) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a Python code refactoring assistant. "
                "Return ONLY the refactored code. "
                "Do not include explanations, comments, code fences, or additional text."
            ),
        },
        {
            "role": "user",
            "content": (
                "Refactor the following Python code by removing all unnecessary whitespace outside of print strings. "
                "Preserve necessary indentation to maintain code blocks. "
                "Do not remove or alter spacing inside string literals in print statements. "
                "Remove spaces around operators, commas, parentheses, colons, and semicolons where possible. "
                "Do not add explanations, comments, or additional text. Return only the code.\n\n"
                f"{code_str}"
            ),
        },
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.0,
        max_tokens=3000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].message.content

def finalize_prints(code_str: str, client: OpenAI) -> str:
    # Make print blocks as concise as possible, omit headers like PASS/FAIL, etc.
    # We assume headers are uppercase or words like "PASS:", "FAIL:", "Input:" and we want to remove them.
    # Just print the essential info. No explanations, comments, or additional text.
    messages = [
        {
            "role": "system",
            "content": (
                "You are a Python code refactoring assistant. "
                "Return ONLY the refactored code. "
                "Do not include explanations, comments, code fences, or additional text."
            ),
        },
        {
            "role": "user",
            "content": (
                "Refactor the following Python code so that print statements are as concise as possible "
                "and omit any header-like prefixes (e.g., PASS:, FAIL:, Input:) or extraneous labeling. "
                "Retain only essential result information in lowercase. "
                "Do not add explanations, comments, or additional text. Return only the code.\n\n"
                f"{code_str}"
            ),
        },
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.0,
        max_tokens=3000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].message.content

def remove_comments_and_blank_lines(code: str) -> str:
    final_lines = []
    for line in code.split("\n"):
        if "#" in line:
            line = line[:line.index("#")]
        line = line.rstrip()
        if line.strip():
            final_lines.append(line)
    return "\n".join(final_lines)

def uglify_code(file_path: str, key_file: str = "openai_key.txt"):
    api_key = get_openai_api_key(key_file)
    client = OpenAI(api_key=api_key)

    if not file_path.endswith(".py"):
        print("Error: Input file must be a Python (.py) file.")
        sys.exit(1)

    if not os.path.exists(file_path):
        print("Error: File not found.")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        original_code = f.read()

    minimized_code = minimize_local_variables(original_code, client)
    renamed_code = rename_identifiers(minimized_code, client)
    condensed_code = condense_adjacent_lines(renamed_code, client)
    joined_code = join_if_statements(condensed_code, client)
    lowered_prints_code = enforce_lowercase_prints(joined_code, client)
    whitespace_removed_code = remove_whitespace_outside_prints(lowered_prints_code, client)
    finalized_prints_code = finalize_prints(whitespace_removed_code, client)
    final_code = remove_comments_and_blank_lines(finalized_prints_code)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_code + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python crazy_code.py <path_to_python_file> [optional_key_file]")
        sys.exit(1)
    file_path = sys.argv[1]
    key_file = sys.argv[2] if len(sys.argv) == 3 else "openai_key.txt"
    uglify_code(file_path, key_file)



