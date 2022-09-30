import hashlib
from binascii import hexlify

password_1 = "A demonstration of cryptographic hash function"
password_2 = "Practise makes for proficiency. Doing things over and over again helps mastery"

pass_enc = password_1.encode('utf-8', 'strict')
pass_hex = hexlify(pass_enc)
pass_hash_256 = hashlib.sha256(pass_hex).hexdigest()
pass_hash_512 = hashlib.sha512(pass_hex).hexdigest()

pass_2_enc = password_2.encode('utf-8', 'strict')
pass_2_hex = hexlify(pass_2_enc)
pass_2_hash_256 = hashlib.sha256(pass_2_hex).hexdigest()
pass_2_hash_512 = hashlib.sha512(pass_2_hex).hexdigest()

print()
print("Hexadecimal values of UTF-8 encoded Password_1 and Password_2")
print("Passowrd_1", pass_hex.decode())
print("Password_2", pass_2_hex.decode())

print()
print("SHA-256 values of Password_1 and Password_2")
print("Password_1", pass_hash_256)
print("Password_2", pass_2_hash_256)

print()
print("SHA-512 values of Password_1 and Password_2")
print("Password_1", pass_hash_512)
print("Password_2", pass_2_hash_512)

