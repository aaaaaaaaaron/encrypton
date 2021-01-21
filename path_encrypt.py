import os
from encrypt_gen import *
from encrypt import *

def encrypt_dir(directory, key):
    if os.path.exists(os.path.join(directory.decode(), "encrypted.txt")):
        print("this file has already been encrypted")
    else:  # encrypts directory if it has not been marked as encrypted already
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            # if filename.endswith(".png") or filename.endswith(".txt"):  # only selects two types of files
            if "." in filename:  # this is probably a bad idea.
                print(os.path.join(directory.decode(), filename))
                encrypt(os.path.join(directory.decode(), filename), key)
                continue
            else:
                continue
        with open(os.path.join(directory.decode(), "encrypted.txt"), 'w') as fp:
            fp.write("This directory has been encrypted!")
            pass


if __name__ == "__main__":
    key = load_key()
    directory = os.fsencode("C:/Users/Aaron/Documents/Encryption/EncryptTheseFiles")
    encrypt_dir(directory, key)

