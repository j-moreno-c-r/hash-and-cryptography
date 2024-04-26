from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import binascii

def encrypt_data(password, data):
    # Generate a random salt
    salt = get_random_bytes(AES.block_size)

    # Derive a key from the password
    key = PBKDF2(password, salt, dkLen=32)

    # Create a cipher object
    cipher = AES.new(key, AES.MODE_EAX)

    # Encrypt the data
    ciphertext, tag = cipher.encrypt_and_digest(data)

    # Return the salt, the ciphertext, and the AES tag
    return salt + cipher.nonce + ciphertext + tag

def decrypt_data(password, encrypted_data):
    # Extract the salt, nonce, ciphertext, and tag from the encrypted data
    salt = encrypted_data[:16]
    nonce = encrypted_data[16:32]
    ciphertext = encrypted_data[32:-16]
    tag = encrypted_data[-16:]

    # Derive the key from the password
    key = PBKDF2(password, salt, dkLen=32)

    # Create a cipher object
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    # Decrypt the data
    data = cipher.decrypt_and_verify(ciphertext, tag)

    # Return the decrypted data
    return data