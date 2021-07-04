import hashlib
data = input("enter string: ")
def using_sha224():
    data_hash = hashlib.sha224(data.encode())
    print("Hash using SHA224: ", data_hash.hexdigest())

def using_sha256():
    data_hash = hashlib.sha256(data.encode())
    print("Hash using SHA256: ", data_hash.hexdigest())

def using_sha1():
    data_hash = hashlib.sha1(data.encode())
    print("Hash using SHA1: ", data_hash.hexdigest())

using_sha224()
using_sha256()
using_sha1()
