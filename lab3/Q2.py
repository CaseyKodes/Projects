from Crypto.Hash import SHA256
import os

path = os.listdir('Q2files')
toCheck = '2370f0cf2bb229049f9ff30d1ab7d4e87c5c89328e430c2f63fd944c9c5c0dee'
for file in path:
	toOpen = "Q2files/"+file
	with open (toOpen, 'rb') as f:
		toHash = f.read()

	h = SHA256.new(toHash)
	h = h.hexdigest()
	if h == toCheck:
		print(f"{file} has the same hash value")
		break
