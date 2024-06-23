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

def derive_key_from_passphrase(passphrase, salt):
    """
    Derive a key from the provided passphrase using PBKDF2HMAC
    """
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
    Generate a key for encryption, encrypt it with the passphrase, and save it to a file
    """
    key = Fernet.generate_key()
    salt = os.urandom(16)  # Generate a random salt
    derived_key = derive_key_from_passphrase(passphrase, salt)
    fernet = Fernet(derived_key)
    
    encrypted_key = fernet.encrypt(key)
    
    with open('filekey.key', 'wb') as filekey:
        filekey.write(salt + encrypted_key)  # Store the salt and the encrypted key

    print("Key generated and saved to 'filekey.key'.")

def load_key(passphrase):
    """
    Load the encrypted key from the file, decrypt it using the passphrase, and return the decrypted key
    """
    with open('filekey.key', 'rb') as filekey:
        data = filekey.read()
    salt = data[:16]  # Extract the salt
    encrypted_key = data[16:]  # Extract the encrypted key
    
    derived_key = derive_key_from_passphrase(passphrase, salt)
    fernet = Fernet(derived_key)
    
    key = fernet.decrypt(encrypted_key)
    return key

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
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt files using a passphrase-protected key.")
    parser.add_argument('mode', choices=['generate-key', 'encrypt', 'decrypt'], help="Mode: 'generate-key', 'encrypt', or 'decrypt'")
    parser.add_argument('file', nargs='?', help="Path to the file to encrypt or decrypt")
    parser.add_argument('passphrase', help="Passphrase for key generation and validation")

    args = parser.parse_args()

    if args.mode == 'generate-key':
        generate_key(args.passphrase)
    elif args.mode == 'encrypt':
        if args.file:
            encrypt_file(args.file, args.passphrase)
        else:
            print("Error: You must specify the file to encrypt.")
    elif args.mode == 'decrypt':
        if args.file:
            decrypt_file(args.file, args.passphrase)
        else:
            print("Error: You must specify the file to decrypt.")
