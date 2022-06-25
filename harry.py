import os
from cryptography.fernet import Fernet

# finding the files

files = []

for file in os.listdir():
    # to exclude these files from being decrypted
    if file == ".idea" or file == "voldemort.py" or file == "thekey.key" or file == "harry.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", "rb") as key:
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
