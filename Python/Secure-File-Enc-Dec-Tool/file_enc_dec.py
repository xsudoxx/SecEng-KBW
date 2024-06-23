#!/usr/bin/env python3

"""
The Secure File Encrypter and Decrypter is a Python-based application designed to securely encrypt and decrypt files using strong cryptographic algorithms.
This project aims to provide a practical implementation of file security, ensuring that sensitive information remains protected from unauthorized access.
"""

from cryptography.fernet import Fernet
import argparse
import os

def generate_key():
    """
    Generate a key for encryption and save it to a file
    """

    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    return key

def load_key():
    """
    Load the key from the current directory named `filekey.key`
    """

    return open('filekey.key', 'rb').read()

def encrypt_file(file_path):
    """
    Encrypt the file and write it back to the same location
    """
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        orginal = file.read()

    encrypted = fernet.encrypt(orginal)

    with open(file_path, 'wb') as encrypt_file:
        encrypt_file.write(encrypted)

    print(f"file '{file_path} encrypted successfully'")

def decrypt_file(file_path):
    """
    Decrypte the file and write it back to the same location
    """
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    print(f"File '{file_path}' decrypted successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt files using AES-256 encryption.")
    parser.add_argument('mode', choices=['encrypt','decrypt'], help="Mode = 'encrypt' or 'decrypt'")
    parser.add_argument('file',help="Path to the file to encrypt or decrypt")

    args = parser.parse_args()

    if args.mode == 'encrypt':
        encrypt_file(args.file)
    elif args.mode == 'decrypt':
        decrypt_file(args.file)