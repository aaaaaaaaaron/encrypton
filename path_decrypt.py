import os
from encrypt_gen import *
from decrypt import *

def decrypt_dir(directory, key):
    if not os.path.exists(os.path.join(directory.decode(), "encrypted.txt")):
        print("this directory has not been encrypted, no need to decrypt")
    else:
        os.remove(os.path.join(directory.decode(), "encrypted.txt"))  # removes the marker file to show its no longer en
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            # if filename.endswith(".png") or filename.endswith(".txt"):  # only selects two types of files
            if check_file(filename):
                print(os.path.join(directory.decode(), filename))
                decrypt(os.path.join(directory.decode(), filename), key)
                continue
            else:
                continue


if __name__ == "__main__":
    key = load_key()
    directory = os.fsencode("C:/Users/Aaron/Documents/Encryption/EncryptTheseFiles")
    decrypt_dir(directory, key)

