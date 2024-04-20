from Crypto.PublicKey import RSA

priv_key = RSA.generate(1024)

pub_key = priv_key.public_key()

priv_text = priv_key.export_key()
pub_text = pub_key.export_key()

with open('./Solutions/e.key', 'wb') as f:
    f.write(pub_text)

with open('./Solutions/d.key', 'wb') as f:
    f.write(priv_text)
