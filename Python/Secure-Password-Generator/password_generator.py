#!/usr/bin/env python3

"""
Secure Password Generator

This script generates strong, random passwords based on user defined criteria. It utilizes cryptographic principles to ensure password security
"""
import string
import secrets
import argparse
import pyperclip

DEFAULT_PASSWORD_LENGTH = 12

def generate_password(length = DEFAULT_PASSWORD_LENGTH):
    random_password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation)
                              for i in range(length))
    return random_password


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a secure random password')
    parser.add_argument('-l','--length', type=int, default=DEFAULT_PASSWORD_LENGTH, help='Length of the password (default: 12)')

    args = parser.parse_args()
    password = generate_password(length=args.length)

    pyperclip.copy(password)
    print(f'Generated Password: {password}')
    print('Password copied to clipboard')
