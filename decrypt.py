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


def steps_on_dir(directory, password):
    for name in os.scandir(directory):
        path = os.path.join(directory, name)

        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as Ex:
                print(Ex)
        else:
            steps_on_dir(directory, password)


password = input('enter password: ')
steps_on_dir("C:\cestcrypt", password)
