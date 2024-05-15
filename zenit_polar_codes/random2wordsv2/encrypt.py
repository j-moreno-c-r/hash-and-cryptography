import random
import string 

def decrypt(data, zenit, polar):
    decrypt_dict = {p: z for z, p in zip(zenit, polar)}
    decrypt_dict = {p: z for z, p in zip(zenit, polar)} 
    return ''.join(decrypt_dict.get(c, c) for c in data)

def encrypt(data, zenit, polar):
    encrypt_dict = {z: p for z, p in zip(zenit, polar)}
    encrypt_dict = {z: p for z, p in zip(zenit, polar)}
    return ''.join(encrypt_dict.get(c, c) for c in data)


def generate_two_unique_words(length):
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    word1 = ''.join(letters[:length])
    word2 = ''.join(letters[length:length*2])
    return word1, word2
