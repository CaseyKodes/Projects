from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
from Crypto.Hash import MD5

'''
BLOCKSIZE = 256
h = MD5.new()
count = 0
with open( 'R5.py' , 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        count = count + 1
        h.update(buf)
        buf = afile.read(BLOCKSIZE)

# creating key
hf = h.digest()
of2 = '.key.txt'
file_out = open(of2, "w")
file_out.write("") # Write the varying length ciphertext to the file (this is the encrypted data)
file_out.close()
input = 'p2.txt' # Input file
oUt = 'Encrypted5' #outputted cipher text (can rename)
original = open(input, 'rb')
contents = original.read()
original.close()
cipher = AES.new(hf, AES.MODE_CBC)  #  cipher
ogD = cipher.encrypt(pad((contents), AES.block_size))
final = open(oUt, "wb")
final.write(cipher.iv)
final.write(ogD)
final.close()
'''

BLOCKSIZE = 256
h = MD5.new()
count = 0
with open( 'R5.py' , 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        count = count + 1
        h.update(buf)
        buf = afile.read(BLOCKSIZE)

# creating key
hf = h.digest()

with open('Encrypted5', 'rb') as f:
        iv = f.read(16)
        ct = f.read()

cipher = AES.new(hf, AES.MODE_CBC, iv=iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)
pt = pt.decode('utf-8')
print(pt)
