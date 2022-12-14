from Crypto.Util.number import bytes_to_long
from Cryptodome.Cipher import AES
import os
import gmpy2
from flag import FLAG
from Cryptodome.Util.number import *


def main():
    key = os.urandom(2) * 16  # 32bit
    iv = os.urandom(16)  # 16bit
    print(bytes_to_long(key) ^ bytes_to_long(iv))
    aes = AES.new(key, AES.MODE_CBC, iv)
    enc_flag = aes.encrypt(FLAG)
    print(enc_flag)


if __name__ == "__main__":
    main()
