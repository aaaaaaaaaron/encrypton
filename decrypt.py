"""
Credit: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
"""

from cryptography.fernet import Fernet
from encrypt_gen import *

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

if __name__=="__main__":
    key = load_key()
    # file = "toEncrypt.txt"
    file = "C:/Users/Aaron/Documents/Encryption\EncryptTheseFiles/image.png"
    decrypt(file, key)
