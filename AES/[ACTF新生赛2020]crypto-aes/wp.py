from Crypto.Cipher import AES
import os
from gmpy2 import*
from Crypto.Util.number import*

xor = 91144196586662942563895769614300232343026691029427747065707381728622849079757
enc_flag = b'\x8c-\xcd\xde\xa7\xe9\x7f.b\x8aKs\xf1\xba\xc75\xc4d\x13\x07\xac\xa4&\xd6\x91\xfe\xf3\x14\x10|\xf8p'
out = long_to_bytes(xor)
key = out[:16]*2
# print(key)
iv = bytes_to_long(key[16:])^bytes_to_long(out[16:])
# print(iv)
iv = long_to_bytes(iv)
# print(iv)
aes = AES.new(key,AES.MODE_CBC,iv)
flag = aes.decrypt(enc_flag)
print(flag)
