import hashlib
#program to generate MD5 of string data
def _md5():
    string = input("Enter strings: ")
    hash_string = hashlib.md5(string.encode())
    print("Hash using MD5: ", hash_string.hexdigest())

_md5()