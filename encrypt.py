"""
Credit: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
"""

from cryptography.fernet import Fernet
from encrypt_gen import *
import time

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:  # write to SAME FILE to override. nice.
        file.write(encrypted_data)

if __name__=="__main__":
    # generate and write a new key
    write_key()
    # load the previously generated key
    key = load_key()
    # initialize the Fernet class
    f = Fernet(key)

    # file = "toEncrypt.txt"
    file = "C:/Users/Aaron/Documents/Encryption\EncryptTheseFiles/toEncrypt.txt"
    encrypt(file, key)







    # # encodes a string to make it suitible for encryption (utf-8 codec)
    # message = "some secret message".encode()
    # # encrypt the message
    # encrypted = f.encrypt(message)
    #
    # # print how it looks
    # print(encrypted)  # prints some crazy string o:
    #
    # # decrypts and encrypts using same class
    # decrypted_encrypted = f.decrypt(encrypted)
    # print(decrypted_encrypted)