#!/usr/bin/env python3

"""
Secure Password Generator

This script generates strong, random passwords based on user defined criteria. It utilizes cryptographic principles to ensure password security
"""
import string
import secrets
import argparse

DEFAULT_PASSWORD_LENGTH = 12

def generate_password(length = DEFAULT_PASSWORD_LENGTH):
    random_password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation)
                              for i in range(length))
    return random_password


if __name__ == "__main__":
    password = generate_password(16)
    print(f'Generated Password: {password}')
