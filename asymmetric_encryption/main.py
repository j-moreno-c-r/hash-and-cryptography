from generate_keys import generate_keys
from encrypt_decrypt import encrypt, decrypt


if __name__ == '__main__':
    if __name__ == '__main__':
        private_key, public_key = generate_keys()
        #public_key, private_key = organize_keys(privkey, pubkey)
        message = input("Enter a message: ").encode()
        encrypted = encrypt(public_key, message)
        print("Encrypted:", encrypted)
        original_message = decrypt(private_key, encrypted)
        print("Decrypted:", original_message)