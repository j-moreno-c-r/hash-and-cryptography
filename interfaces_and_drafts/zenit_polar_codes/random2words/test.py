zenit = "zenit"
polar = "polar"

encrypt_dict = {z: p for z, p in zip(zenit, polar)}
decrypt_dict = {p: z for z, p in zip(zenit, polar)}

def encrypt(data):
    return ''.join(encrypt_dict.get(c, c) for c in data)

def decrypt(data):
    return ''.join(decrypt_dict.get(c, c) for c in data)
    
print(encrypt("hello"))