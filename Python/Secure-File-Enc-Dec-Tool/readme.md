# Secure File Encryption and Decryption Tool

Welcome to the Secure File Encryption and Decryption Tool project! This Python-based application allows users to encrypt and decrypt files securely using strong cryptographic algorithms.

## Features

- **File Encryption**: Encrypt files using AES-256 encryption algorithm.
- **File Decryption**: Decrypt encrypted files securely.
- **Password-based Encryption**: User-defined passphrase for encryption and decryption.
- **Error Handling**: Robust error handling for file operations and cryptographic functions.

## installation
### install dependencies
````
pip3 install -r requirements.txt
````
### Generate an Encryption Key:
````
python3 -c "from file_enc_dec import generate_key; generate_key()"
````


## Usage
## Encrypting a File
To encrypt a file, run the following command:
````
python3 encrypt.py -f <path_to_file> -p <passphrase>
````
Replace <path_to_file> with the path to the file you want to encrypt.
Replace <passphrase> with your chosen passphrase for encryption.
## Decrypting a File
To decrypt an encrypted file, use the following command:
````
python3 decrypt.py -f <path_to_encrypted_file> -p <passphrase>
````
Replace <path_to_encrypted_file> with the path to the encrypted file.
Use the same <passphrase> used during encryption.

## Security Considerations
- Encryption Strength: Uses AES-256 encryption, considered secure for protecting sensitive data.
- Passphrase Handling: Ensure to use strong passphrases and store them securely.
- File Integrity: Validate decrypted files to prevent data corruption.

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug fixes, please submit a pull request or open an issue.
