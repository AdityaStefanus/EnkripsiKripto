# Aditya Stefanus
# 312010048
#Enkripsi XOR
def encrypt(plaintext, key):
  ciphertext = ""
  for i in range(len(plaintext)):
    ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
  return ciphertext

# Menggunakan XOR untuk deskripsi
def decrypt(ciphertext, key):
  plaintext = ""
  for i in range(len(ciphertext)):
    plaintext += chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
  return plaintext

# Mencoba enkripsi dan deskripsi
plaintext = "Halo, ini adalah teks asli"
key = "sandi"

ciphertext = encrypt(plaintext, key)
print("Teks terenkripsi:", ciphertext)

decrypted = decrypt(ciphertext, key)
print("Teks yang didekripsi:", decrypted)