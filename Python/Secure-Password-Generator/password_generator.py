#!/usr/bin/env python3

"""
Secure Password Generator

This script generates strong, random passwords based on user defined criteria. It utilizes cryptographic principles to ensure password security
"""
import string
import secrets

DEFAULT_PASSWORD_LENGTH = 12

def generate_password(length = DEFAULT_PASSWORD_LENGTH):
    random_password = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                              for i in range(length))
    print(random_password)


if __name__ == "__main__":
    generate_password()
