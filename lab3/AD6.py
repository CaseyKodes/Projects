from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from base64 import *
import sys

priv_contents = 'MIICWwIBAAKBgQDKif5MmN8I6i8CJqWl/ye/f2c71s3XS/w5nwSnzbPeNAhMkS0QyNQy36lLCNsJWU81VPsKrdLkerjvakleRCOvHSJnTjiLV9CIdG45RPct82AdmWFdRwjzZPYWSFqAj8f0mxpwYO0+m6kuvFeTgIezWaD++SOgPOQ4atPiKRmncQIDAQABAoGAM2SHg/0oXvU5X2TaFIBloBheZBcx3QcZZa+deUzfbqsqTe9qjX9AJPaO2QzSs5EXYbOCDegkgrhHM+z21/YXTXRQehC2JPOBZOcUOV8UMrFPRHVP3D+O0fq3qdREih7edO8I/Q96MTW60p/GRSy759NDs1fLtwBl9j9KOdqUcP8CQQDOv0bpnnSLBDJfdeFXqGe3wpaOggtEmwL0gi+4xpubFmMAPEEXzS3D/TveX2yHx9Lac3HVsYvmox6bx3UeTSPDAkEA+soT9YtDBo1p0V8jzgh22hXOlh3pqwEGFUcSVe+H5A0ZSmsYYSD6l1aY2tx/QhJMGbySGHILSIfjr6b3p9zYuwJAFN1s9KrPLDByPPwSj9wpC3yR4TPymyvhsndpBYbVsWMi/qUWFKbaVYs6/Yg31cQu3WkFNgHDErWnoyUQBszWLQJAGFCTUtEntHDte4Ev5X/olghbOS65Qv0ca9+yJWbN1Ax5EUAE4xXhdd7Nfxq1s+A2RKCFwZz8/xE9v//+LuY4lQJAUq/P+5iSiLYLDo0IhLp829zDVpD57FtS/ZiFjSZ+sIJIpruERE9u8vX6tVfBlmmWbRqO2y0OOcP7bA8WEppqyA=='
pr_k = open("Solutions/d.key", "rb").read()

priv_key = RSA.import_key(pr_k)

if len(sys.argv) != 2:
    exit(0)

with open(f"./{sys.argv[1]}", "rb") as f:
    contents = f.read()
    decrypt = PKCS1_OAEP.new(priv_key)
    k = decrypt.decrypt(contents)
    str_k = b64encode(k)
    print(str(str_k))

