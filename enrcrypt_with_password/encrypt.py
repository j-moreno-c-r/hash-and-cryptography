cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
text = cipher_dec.decrypt_and_verify(ciphertext, tag)