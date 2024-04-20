from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

variable = b'k\xfc\x19\x8b\xd1R.\xf5\xc0Mp1Q\xcd\xa7w'
var = str(variable)

with open('Encrypted4', 'rb') as f:
	iv = f.read(16)
	ct = f.read()

cipher = AES.new(variable, AES.MODE_CBC, iv=iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)
pt = pt.decode('utf-8')
print(pt)
