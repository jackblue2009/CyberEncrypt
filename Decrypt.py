from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        iv = file_in.read(16)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        cipherTxt = file_in.read()

        decrypted_data = cipher.decrypt(cipherTxt)

        unpadded_data = unpad(decrypted_data, 16)
        file_out.write(unpadded_data)

def decrypt_dir(directory, key):
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file_name in files:
            if file_name.startswith("encrypted_"):
                input_file = os.path.join(root, file_name)
                output_file = os.path.join(root, file_name.replace("encrypted_", ""))
                
                # Decrypt the file
                decrypt_file(input_file, output_file, key)
                
                # Delete the encrypted file
                os.remove(input_file)

#input_file = "hidden.txt"
#output_file = "solved.txt"
#directory = "C:/"
directory = "dir"
key = b'YourSecretKey123'

decrypt_dir(directory, key)

""" for filename in os.listdir(directory):
    if filename.startswith("Encrypted_"):
        input_file = os.path.join(directory, filename)
        output_file = os.path.join(directory, filename.replace("Encrypted_", ""))

        decrypt_file(input_file, output_file, key)
        os.remove(input_file) """