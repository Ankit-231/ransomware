import os
from cryptography.fernet import Fernet

files = []

files_path = "files_/"

for file in os.listdir("files_"):
    # os.path.join(files_path, file) is written to give full path of boat.txt though the condition itself isn't
    # necessary considering only files will be kept in files_

    if os.path.isfile(os.path.join(files_path, file)):
        files.append(files_path + file)

with open("key/thekey.key", "rb") as key:
    secretkey = key.read()

# our password

secret_phrase = "coffee"

user_phrase = input("Enter your password:\n")

if user_phrase == secret_phrase:
    # going through all the files, i.e, boat.txt, etc.
    for file in files:
        # opening boat.txt in read binary mode and calling boat.txt as "thefile" now
        # remember that file is also boat.txt now
        with open(file, "rb") as thefile:
            # contents is now boat.txt
            contents = thefile.read()
            # contents_decrypted is now the boat.txt file decrypted with the secret
            contents_decrypted = Fernet(secretkey).decrypt(contents)

        # opening boat.txt in wb as thefile
        with open(file, "wb") as thefile:
            # overwriting the contents of boat.txt with contents_decrypted
            thefile.write(contents_decrypted)
    print("Congratulations, your files have been decrypted. Enjoy your coffee.")

else:
    print("Wrong password!")
