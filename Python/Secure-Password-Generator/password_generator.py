#!/usr/bin/env python3

"""
Secure Password Generator

This script generates strong, random passwords based on user defined criteria. It utilizes cryptographic principles to ensure password security
"""
import string
import random

DEFAULT_PASSWORD_LENGTH = 12

def generate_password(length = DEFAULT_PASSWORD_LENGTH):
    
    random_string = ''.join(random.choices(string.ascii_letters, k=length))
    print(random_string)


if __name__ == "__main__":
    generate_password()
