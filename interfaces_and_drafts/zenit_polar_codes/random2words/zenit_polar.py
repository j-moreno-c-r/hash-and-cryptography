import random
import string

def generate_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def decrypt(data, zenit, polar):
    decrypt_dict = {p: z for z, p in zip(zenit, polar)}
    decrypt_dict = {p: z for z, p in zip(zenit, polar)} 
    return ''.join(decrypt_dict.get(c, c) for c in data)

def encrypt(data, zenit, polar):
    encrypt_dict = {z: p for z, p in zip(zenit, polar)}
    encrypt_dict = {z: p for z, p in zip(zenit, polar)}
    return ''.join(encrypt_dict.get(c, c) for c in data)

test_word = input("Enter a word to encrypt: ")
zenit = generate_random_word(5)
polar = generate_random_word(5)
print(encrypt(test_word, zenit, polar))
print(decrypt(test_word, zenit, polar))
print(zenit)
print(polar)
