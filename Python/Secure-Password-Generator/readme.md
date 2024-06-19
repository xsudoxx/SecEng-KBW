# Secure Password Generator

## Overview

The Secure Password Generator is a Python script that generates strong, random passwords following best practices for password security. It uses cryptographic principles to ensure the passwords generated are difficult to guess and secure for use in various applications.

## Features

- **Generate Password:** Creates a random password based on specified criteria (length, complexity).
- **Copy to Clipboard:** Option to copy the generated password to the clipboard for easy use.
- **Customizable Settings:** Allow users to customize password length and include/exclude specific character sets (uppercase, lowercase, digits, symbols).
- **Command-line Interface (CLI):** Implement the generator as a command-line tool for easy integration into scripts or workflows.

## Security Principles

- **Randomness:** Utilize Python's `secrets` module for secure random number generation.
- **Character Sets:** Provide options to include uppercase letters, lowercase letters, digits, and symbols to enhance password complexity.
- **Secure Output:** Ensure generated passwords are not stored in plain text and are securely transferred if copied to the clipboard.

## Installation

### Prerequisites

- Python 3.x installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

### Dependencies

Install the required dependencies using pip3:

````
pip3 install -r requirements.txt
````

## File Structure
````
secure_password_generator/
│
├── password_generator.py     # Main script for generating passwords
├── README.md                 # Project documentation
├── LICENSE                   # License file (e.g., MIT License)
└── requirements.txt          # List of dependencies
````

## Example Usage
````
python password_generator.py -l 16
````
-l, --length: Specifies the length of the password. In this example, we set it to 16 characters.

## Example Output
````
Generated Password: hE$1M^t2P9F!gS#7B
Password copied to clipboard.
````