import hashlib
def encrypter(prhase):
    while True:
          result = hashlib.sha256(prhase.encode()).hexdigest()
          print(result)
          return result

