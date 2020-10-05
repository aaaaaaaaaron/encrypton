import os
from encrypt_gen import *
from decrypt import *

def encrypt_dir(directory, key):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".png") or filename.endswith(".txt"):  # only selects two types of files
            print(os.path.join(directory.decode(), filename))
            decrypt(os.path.join(directory.decode(), filename), key)
            continue
        else:
            continue


if __name__ == "__main__":
    key = load_key()
    directory = os.fsencode("C:/Users/Aaron/Documents/Encryption/EncryptTheseFiles")
    encrypt_dir(directory, key)

