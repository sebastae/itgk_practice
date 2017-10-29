#!/usr/bin/env python3.6

import binascii
from random import shuffle


def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)


def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def encrypt(msg, key):
    msg = toHex(msg)
    key = toHex(key)

    code = msg ^ key
    return code

def decrypt(code, key):
    key = toHex(key)
    msg = ""

    msg = code ^ key
    return toString(msg)

def main():
    msg = input("Write a sentence: ")
    key = [l for l in msg]
    shuffle(key)
    key = bytes("".join(key), encoding="ascii")
    msg = bytes(msg, encoding="ascii")

    emsg = encrypt(msg, key)
    dmsg = decrypt(emsg, key)

    print("Encrypted message:", emsg)
    print("Decrypted message:", dmsg)

if __name__ == "__main__":
    main()