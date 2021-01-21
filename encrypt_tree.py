"""
This file contains code that will encrypt the files inside of a directory, and inside of any directories inside
that directory, recursively.

https://stackabuse.com/introduction-to-python-os-module/
"""

from path_encrypt import *

def encrypt_tree(directory, key):
    for file in os.listdir(directory):  # looks at everything in given directory
        filename = os.fsdecode(file)
        fullpath = os.path.join(directory.decode(), filename)  # turns it into a readable path
        if os.path.isdir(fullpath):  # if it is a folder ("directory")
            print(fullpath)
            encrypt_tree(os.fsencode(fullpath), key)  # recursive step
    encrypt_dir(directory, key)  # now that its at the bottom of the "tree" it encrypts the directory



if __name__=="__main__":
    key = load_key()
    directory = os.fsencode("C:/Users/Aaron/Documents/Encryption/EncryptTheseFiles")
    encrypt_tree(directory, key)
