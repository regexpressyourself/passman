import base64
from Crypto.Cipher import AES
from Crypto import Random

def encrypt(raw, key):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

def decrypt(enc, key):
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
    return result

def pad(s):
    bs = 32
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

