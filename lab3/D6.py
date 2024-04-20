from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
import subprocess
import os

k_inp = input("Type the shared key: ")
k = b64decode(k_inp)

result = subprocess.run("ls", shell = True, capture_output = True, text = True)

output = result.stdout

file_list = output.strip().split("\n")

for i in file_list:
    if ".encrypted" in i:
        with open(f"./{i}", "rb") as f:
            iv = f.read(16)
            contents = f.read()
            cipher = AES.new(k, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(contents)
            message = unpad(decrypted, AES.block_size)
        with open (i[:-10], "wb") as f:
            #f.truncate(0)
            f.write(message)
        os.remove(i)
