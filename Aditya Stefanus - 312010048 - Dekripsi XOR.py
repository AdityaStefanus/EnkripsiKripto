#Aditya Stefanus
# 312010048
#Dekripsi
# Menggunakan XOR untuk enkripsi
def encrypt(plaintext, key):
  ciphertext = ""
  for i in range(len(plaintext)):
    ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
  return ciphertext

# Mengunakan XOR untun deskripsi
def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(plaintext)):
        plaintext += chr(ord(plaintext[i]) ^ ord())
    return

# Mencoba enkripsi dan deskripsi
plaintext = "Hallo, Ini adalah text asli"
key = "sandi"

ciphertext = encrypt(plaintext, key)
print ("Teks terenkripsi", ciphertext)

decrypt(ciphertext, key)
print ("Teks terdekripsi", decrypt)