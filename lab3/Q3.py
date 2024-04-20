from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import os

def verify_sig(key, data, sig, filename):
	h = SHA256.new(data)
	rsa = RSA.importKey(key)
	signer = PKCS1_v1_5.new(rsa)
	with open(sig, 'rb') as f:
		signature = f.read()
	if (signer.verify(h, signature)):
		print(f"Success: {filename}")

exefiles = []
with open('Q3pk.pem', 'r') as f:
	key = f.read()

for exe in os.listdir('Q3files'):
	if exe.endswith('.exe'):
		exefiles.append(exe)
for file in exefiles:
	with open('Q3files/'+file, 'rb') as f:
		data = f.read()
	sig = 'Q3files/' + file + '.sign'
	verify_sig(key, data, sig, file)
