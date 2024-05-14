import random
import string

def generate_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def encrypt(data, zenit, polar):
    encrypt_dict = {z: p for z, p in zip(zenit, polar)}
    return ''.join(encrypt_dict.get(c, c) for c in data)

def decrypt(data, zenit, polar):
    decrypt_dict = {p: z for z, p in zip(zenit, polar)}
    return ''.join(decrypt_dict.get(c, c) for c in data)

def encrypt_decrypt(word):
    zenit = generate_random_word(5)
    polar = generate_random_word(5)
    encrypted_word = encrypt(word, zenit, polar)
    decrypted_word = decrypt(encrypted_word, zenit, polar)
    return encrypted_word, decrypted_word, zenit, polar