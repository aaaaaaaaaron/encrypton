"""
This file contains code that will encrypt the files inside of a directory, and inside of any directories inside
that directory, recursively.

https://stackabuse.com/introduction-to-python-os-module/
"""

from path_encrypt import *

def encrypt_tree(directory, key):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        fullpath = os.path.join(directory.decode(), filename)
        if os.path.isdir(fullpath):
            print(fullpath)
            encrypt_tree(os.fsencode(fullpath), key) # I might be able to get rid of the redundant encoding.
    encrypt_dir(directory, key)



if __name__=="__main__":
    key = load_key()
    directory = os.fsencode("C:/Users/Aaron/Documents/Encryption/EncryptTheseFiles")
    encrypt_tree(directory, key)
