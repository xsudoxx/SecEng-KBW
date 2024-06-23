#!/usr/bin/env python3

"""
The Secure File Encrypter and Decrypter is a Python-based application designed to securely encrypt and decrypt files using strong cryptographic algorithms.
This project aims to provide a practical implementation of file security, ensuring that sensitive information remains protected from unauthorized access.
"""

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import argparse
import os
import base64

def derive_key_from_passphrase(passphrase):
    """
    Derive a key from the provided passphrase using PBKDF2HMAC
    """
    salt = b'\x1f\x87\xef\x3e\x4c\x92\xaf\xb3'  # You should generate a new random salt for each key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(passphrase.encode()))
    return key

def generate_key(passphrase):
    """
    Generate a key for encryption based on the passphrase and save it to a file
    """
    key = derive_key_from_passphrase(passphrase)
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

def load_key(passphrase):
    """
    Load the key from the current directory named `filekey.key` and validate it using the passphrase
    """
    stored_key = open('filekey.key', 'rb').read()
    derived_key = derive_key_from_passphrase(passphrase)
    if stored_key != derived_key:
        raise ValueError("Incorrect passphrase")
    return derived_key

def encrypt_file(file_path, passphrase):
    """
    Encrypt the file and write it back to the same location
    """
    key = load_key(passphrase)
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"File '{file_path}' encrypted successfully.")

def decrypt_file(file_path, passphrase):
    """
    Decrypt the file and write it back to the same location
    """
    key = load_key(passphrase)
    fernet = Fernet(key)

    with open(file_path, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    print(f"File '{file_path}' decrypted successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt files using a passphrase-based key.")
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help="Mode: 'encrypt' or 'decrypt'")
    parser.add_argument('file', help="Path to the file to encrypt or decrypt")
    parser.add_argument('passphrase', help="Passphrase for key generation and validation")

    args = parser.parse_args()

    if args.mode == 'encrypt':
        encrypt_file(args.file, args.passphrase)
    elif args.mode == 'decrypt':
        decrypt_file(args.file, args.passphrase)
