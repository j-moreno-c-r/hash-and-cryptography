from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest('text to encrypt'.encode())

cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
text = cipher_dec.decrypt_and_verify(ciphertext, tag)