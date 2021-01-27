from cryptography.fernet import Fernet


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def check_file(name):
    """
    Checks the file extension to make sure it is a good one to be encrypted. This is a dumb place to put this
    function but eventually I will condense it all.
    :return: Boolean, true if the file should be encrpyted
    """
    # with help from https://www.computerhope.com/issues/ch001789.htm
    extensions = [".txt", ".png", ".aif", ".cda", ".mid", ".midi", ".mp3", ".mp4", ".mpa", ".ogg", ".wav", ".wma",
                  ".wpl", ".7z", ".arj", ".deb", ".pkg", ".tar.gz", ".z", ".zip", ".csv", ".dat", ".dat", ".dbf",
                  ".log", ".sql", ".tar", ".email", ".eml"]
    for extension in extensions:
        if name.endswith(extension):
            return True
    return False


if __name__ == "__main__":
    write_key()
